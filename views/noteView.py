from PySide6 import QtCore
from PySide6.QtWidgets import QWidget

from views.subView.noteViewContent import NoteViewContent
from views.subView.noteViewCategory import NoteViewCategory


class NoteView(QWidget):
    action_signal = QtCore.Signal(str, str)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.notes_category = NoteViewCategory(self)
        self.notes_category.action_signal.connect(self.deal_with_action)

        self.notes_content = NoteViewContent(self)
        self.notes_content.action_signal.connect(self.deal_with_action)

        self.set_mode('Add new note Category')

    def set_mode(self, mode):
        print('mode :: ', mode)
        if mode == 'Add new note Category':
            self.notes_category.show()
            self.notes_content.hide()
        else:
            self.notes_category.hide()
            self.notes_content.show()
            self.notes_content.set_category(mode)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.notes_category.resize(self.width(), self.height())
        self.notes_content.resize(self.width(), self.height())

    def deal_with_action(self, action, name):
        print('action :: ', action, ':', name)
        self.action_signal.emit(action, name)
