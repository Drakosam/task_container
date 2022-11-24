from PySide6.QtWidgets import QWidget

from components.leftMenu import LeftMenu
from utylity.signalNames import SignalNames
from views.noteView import NoteView
from views.settingsView import SettingsView

import utylity.fileManager as fM
from views.todoView import ToDoView


class MainView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        fM.load_from_file()
        self.resize(800, 600)
        self.leftMenu = LeftMenu(self)
        self.leftMenu.selected_signal.connect(self.selected_content)

        self.noteView = NoteView(self)
        self.settingsView = SettingsView(self)
        self.to_do_view = ToDoView(self)

        self.settingsView.hide()
        self.to_do_view.hide()

        self.noteView.action_signal.connect(self.deal_with_action)
        self.to_do_view.action_signal.connect(self.deal_with_action)

    def resizeEvent(self, event):
        self.leftMenu.resize(250, self.height())

        self.noteView.resize(self.width() - 250, self.height())
        self.settingsView.resize(self.width() - 250, self.height())
        self.to_do_view.resize(self.width() - 250, self.height())

        self.noteView.move(250, 0)
        self.settingsView.move(250, 0)
        self.to_do_view.move(250, 0)

    def selected_content(self, content, name):
        if content == 'note':
            self.hide_all()
            self.noteView.show()
            self.noteView.set_mode(name)

        elif content == 'todo':
            self.hide_all()
            self.to_do_view.show()
            self.to_do_view.set_mode(name)

        elif content == 'settings':
            self.hide_all()
            self.settingsView.show()

    def hide_all(self):
        self.to_do_view.hide()
        self.noteView.hide()
        self.settingsView.hide()

    def note_action(self, name: SignalNames):
        if name == SignalNames.NEW_CATEGORY.value:
            self.leftMenu.refresh_view()
        elif name == SignalNames.REMOVE_CATEGORY.value:
            self.leftMenu.refresh_view()

    def deal_with_action(self, action, name):
        if action == 'notes':
            self.note_action(name)
            fM.save_to_file()
        if action == 'todo':
            fM.save_to_file()

