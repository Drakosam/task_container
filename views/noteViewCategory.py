from PySide6 import QtCore
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout

from components.customScrollArea import CustomScrollArea
from utylity import organizer
from utylity.signalNames import SignalNames


class NoteViewCategory(QWidget):
    action_signal = QtCore.Signal(str, str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.label = QLabel('Category name :: ', self)
        self.input_name = QLineEdit(self)
        self.button = QPushButton('Create', self)
        self.label.resize(100, 30)
        self.input_name.move(100, 0)
        self.button.move(0, 30)
        self.layout = QHBoxLayout()
        label2 = QLabel('::: Categories :::')
        self.layout_area = QWidget(self)
        self.layout_area.move(0, 60)
        self.layout_area.setLayout(self.layout)
        self.layout.addWidget(label2)
        self.layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.scroll_area = CustomScrollArea(self)
        self.scroll_area.move(0, 90)

        self.button.pressed.connect(self.set_new_category)
        self.refresh_category_list()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.input_name.resize(self.width() - 100, 30)
        self.button.resize(self.width(), 30)
        self.layout_area.resize(self.width(), 30)
        self.scroll_area.resize(self.width(), self.height() - 90)

    def set_new_category(self):
        result = organizer.add_notes_new_category(self.input_name.text())
        if result:
            self.input_name.setText('')
            print('success')
            self.action_signal.emit('notes', SignalNames.NEW_CATEGORY.value)
            self.refresh_category_list()
        else:
            print('fail')

    def refresh_category_list(self):
        self.scroll_area.clear()
        for name in organizer.get_notes_categories():
            button = QPushButton(f'remove :: {name}', self)
            button.setMinimumHeight(40)
            button.pressed.connect(lambda name=name: self.remove_action(name))
            self.scroll_area.add_widget(button)

    def remove_action(self, name):
        organizer.remove_notes_category(name)
        self.action_signal.emit('notes', SignalNames.REMOVE_CATEGORY.value)
        self.refresh_category_list()
