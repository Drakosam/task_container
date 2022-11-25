from functools import partial

from PySide6 import QtCore
from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QTextEdit, QVBoxLayout, QPushButton

from components.customScrollArea import CustomScrollArea
from utylity import organizer
from utylity.signalNames import SignalNames


class ToDoViewList(QWidget):
    action_signal = QtCore.Signal(str, str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.todo_name = QLineEdit(self)
        self.todo_content = QTextEdit(self)
        self.scroll_area = CustomScrollArea(self)
        self.action_area = QWidget(self)
        self.layout_area = QVBoxLayout(self.action_area)

        self.btt_update = QPushButton('Update')
        self.btt_update.setMinimumHeight(35)
        self.btt_update.clicked.connect(self.update_item)

        self.btt_done = QPushButton('Mark as done')
        self.btt_done.setMinimumHeight(35)
        self.btt_done.clicked.connect(self.mark_as_done)

        self.btt_delete = QPushButton('Delete')
        self.btt_delete.setMinimumHeight(35)
        self.btt_delete.clicked.connect(self.delete_item)

        self.todo_name.move(5, 5)
        self.todo_content.move(5, 35)

        self.layout_area.addWidget(self.btt_update)
        self.layout_area.addWidget(self.btt_done)
        self.layout_area.addWidget(self.btt_delete)

        self.selected_id = 0
        self.mode = True

    def set_mode(self, mode):
        self.todo_name.setText('')
        self.todo_content.setText('')
        self.selected_id = 0

        active = mode == 'List'
        self.mode = active
        self.refresh_data()

        if active:
            self.btt_done.setText('Mark as done')
        else:
            self.btt_done.setText('Mark as active')

    def select_item(self, item_id):
        status, item = organizer.get_to_do_with_id(item_id)
        if status:
            self.todo_name.setText(item.name)
            self.todo_content.setText(item.description)
            self.selected_id = item_id

    def update_item(self):
        if self.selected_id != 0:
            print('update')
            organizer.update_todo(self.todo_name.text(), self.todo_content.toPlainText(), self.selected_id,
                                  self.mode)
            self.action_signal.emit('todo', SignalNames.ITEM_UPDATE)

    def delete_item(self):
        if self.selected_id != 0:
            organizer.delete_todo_with_id(self.selected_id)
            self.todo_name.setText('')
            self.todo_content.setText('')
            self.selected_id = 0
            self.refresh_data()

            self.action_signal.emit('todo', SignalNames.ITEM_DELETE)

    def mark_as_done(self):
        if self.selected_id != 0:
            status, item = organizer.get_to_do_with_id(self.selected_id)
            if status:
                organizer.update_todo(item.name, item.description, item.item_id, not item.active)
                self.refresh_data()
                self.todo_name.setText('')
                self.todo_content.setText('')
                self.selected_id = 0
                self.action_signal.emit('todo', SignalNames.ITEM_UPDATE)

    def refresh_data(self):
        self.scroll_area.clear()

        for item in organizer.todos:
            if item.active == self.mode:
                new_btt = QPushButton(item.name)
                new_btt.setMinimumHeight(30)
                new_btt.clicked.connect(partial(self.select_item, item.item_id))
                self.scroll_area.add_widget(new_btt)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.todo_name.resize(self.width() - 10, 30)
        self.todo_content.resize(self.width() - 10, self.height() - 335)

        self.scroll_area.resize(int(self.width() / 2) - 5, 300)
        self.action_area.resize(int(self.width() / 2) - 5, 300)

        self.scroll_area.move(5, self.height() - 300)
        self.action_area.move(int(self.width() / 2), self.height() - 300)
