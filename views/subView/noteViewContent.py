from functools import partial

from PySide6 import QtCore
from PySide6.QtWidgets import QWidget, QTextEdit, QLineEdit, QPushButton, QVBoxLayout

from components.customScrollArea import CustomScrollArea
from utylity import organizer
from utylity.signalNames import SignalNames


class NoteViewContent(QWidget):
    action_signal = QtCore.Signal(str, str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.note_name = QLineEdit(self)
        self.note_content = QTextEdit(self)
        self.notes_list = CustomScrollArea(self)
        self.action_area = QWidget(self)

        self.note_name.move(5, 5)
        self.note_content.move(5, 35)
        self.notes_list.move(5, self.height() - 300)

        self.layout_area = QVBoxLayout(self.action_area)

        update_btt = QPushButton('Update', self.action_area)
        update_btt.setMinimumHeight(35)
        update_btt.clicked.connect(self.update_action)

        clone_btt = QPushButton('Clone', self.action_area)
        clone_btt.setMinimumHeight(35)
        clone_btt.clicked.connect(self.clone_action)

        clear_btt = QPushButton('Clear', self.action_area)
        clear_btt.setMinimumHeight(35)
        clear_btt.clicked.connect(self.clear_action)

        delete_btt = QPushButton('Delete', self.action_area)
        delete_btt.setMinimumHeight(35)
        delete_btt.clicked.connect(self.delete_action)

        self.layout_area.addWidget(update_btt)
        self.layout_area.addWidget(clone_btt)
        self.layout_area.addWidget(clear_btt)
        self.layout_area.addWidget(delete_btt)

        self.category_name = ''
        self.current_note_id = 0

    def resizeEvent(self, event):
        super().resizeEvent(event)

        self.note_name.resize(self.width() - 10, 30)
        self.note_content.resize(self.width() - 10, self.height() - 335)

        self.notes_list.resize(int((self.width() - 10) / 2), 300)
        self.notes_list.move(5, self.height() - 300)

        self.action_area.resize(int((self.width() - 10) / 2), 300)
        self.action_area.move(self.notes_list.width() + 5, 300)

    def update_action(self):
        new_task_name = self.note_name.text()
        task_content = self.note_content.toPlainText()

        status, note_id = organizer.update_note_content(self.category_name, new_task_name, task_content,
                                                        self.current_note_id)

        print('update_action', status)
        if status:
            self.action_signal.emit('notes', SignalNames.ITEM_UPDATE.value)
            self.current_note_id = note_id
        self.refresh_task_list()

    def clone_action(self):
        new_task_name = self.note_name.text()
        task_content = self.note_content.toPlainText()

        status = organizer.update_note_content(self.category_name, new_task_name, task_content, 0)
        if status:
            self.action_signal.emit('notes', SignalNames.ITEM_UPDATE.value)

        self.refresh_task_list()

    def delete_action(self):
        status = organizer.delete_note_content(self.current_note_id)

        self.clear_action()
        if status:
            self.action_signal.emit('notes', SignalNames.ITEM_DELETE.value)

        self.refresh_task_list()

    def clear_action(self):
        self.note_name.setText('')
        self.note_content.setText('')
        self.current_note_id = 0

    def refresh_task_list(self):
        self.notes_list.clear()
        for note in organizer.get_notes_from_category(self.category_name):
            button = QPushButton()
            button.setText(note.name)
            self.notes_list.add_widget(button)
            button.clicked.connect(partial(self.set_note_content, note.note_id))

    def set_category(self, category_name):
        self.category_name = category_name
        self.refresh_task_list()

    def set_note_content(self, note_id):
        note = organizer.get_note(note_id)
        self.current_note_id = note.note_id
        self.note_name.setText(note.name)
        self.note_content.setText(note.content)
        print('set_note_content', note_id)
