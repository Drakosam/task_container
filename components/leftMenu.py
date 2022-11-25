from PySide6 import QtCore
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QWidget, QPushButton

from components.containerButtons import ContainerButton
from components.customScrollArea import CustomScrollArea
from utylity import organizer
from utylity.signalNames import SignalNames


class LeftMenu(QWidget):
    selected_signal = QtCore.Signal(str, str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAutoFillBackground(True)
        q_palette = self.palette()
        q_palette.setColor(self.backgroundRole(), '#333333')
        self.setPalette(q_palette)

        self.scroll_view = CustomScrollArea(self)

        self.notes_button = None
        self.todo_button = None

        self.set_view()

        self.selected = ''

    def set_view(self):
        button_settings = QPushButton('Settings')
        button_settings.setFixedHeight(40)
        font_settings = QFont()
        font_settings.setBold(True)
        font_settings.setPointSize(12)
        button_settings.setFont(font_settings)
        button_settings.pressed.connect(self.settings_signal)

        self.notes_button = ContainerButton('Notes')
        self.notes_button.pick_signal.connect(self.note_signal)
        self.set_note_buttons()

        self.todo_button = ContainerButton('TODO')
        self.todo_button.pick_signal.connect(self.todo_signal)
        self.set_todo_buttons()

        auto_move = QPushButton('Auto Move')
        auto_move.setFixedHeight(40)
        font_settings = QFont()
        font_settings.setBold(True)
        font_settings.setPointSize(12)
        auto_move.setFont(font_settings)
        auto_move.pressed.connect(self.auto_move_signal)

        self.scroll_view.add_widget(self.notes_button)
        self.scroll_view.add_widget(self.todo_button)
        self.scroll_view.add_widget(auto_move)
        self.scroll_view.add_widget(button_settings)

    def set_todo_buttons(self):
        self.todo_button.add_child('List')
        self.todo_button.add_child('Add new')
        self.todo_button.add_child('Done')

    def set_note_buttons(self):
        for name in organizer.get_notes_categories():
            self.notes_button.add_child(name)
        self.notes_button.add_child('Add new note Category')

    def todo_signal(self, event_name, action_name):
        if event_name == SignalNames.GLOBAL_UPDATE.value:
            self.selected_signal.emit('todo', action_name)

    def note_signal(self, event_name, action_name):
        if event_name == SignalNames.LOCAL_UPDATE.value:
            self.selected = action_name
        elif event_name == SignalNames.GLOBAL_UPDATE.value:
            self.selected_signal.emit('note', action_name)

    def auto_move_signal(self):
        self.selected_signal.emit('auto_move', SignalNames.PLACEHOLDER)

    def settings_signal(self):
        self.selected_signal.emit('settings', SignalNames.PLACEHOLDER)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.scroll_view.resize(self.width(), self.height())

    def refresh_view(self):
        self.scroll_view.clear()
        self.set_view()
        print(self.selected)
        if self.selected == 'Notes':
            self.notes_button.expand = True
            self.notes_button.expand_proc()
