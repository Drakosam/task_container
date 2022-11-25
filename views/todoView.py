from PySide6 import QtCore
from PySide6.QtWidgets import QWidget

from views.subView.todoViewList import ToDoViewList
from views.subView.todoViewNew import ToDoViewNew


class ToDoView(QWidget):
    action_signal = QtCore.Signal(str, str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.todo_new = ToDoViewNew(self)
        self.todo_new.action_signal.connect(self.deal_with_action)

        self.todo_list = ToDoViewList(self)
        self.todo_list.action_signal.connect(self.deal_with_action)

        self.todo_list.hide()

    def set_mode(self, mode):
        if mode == 'Add new':
            self.todo_new.show()
            self.todo_list.hide()
        else:
            self.todo_new.hide()
            self.todo_list.show()
            self.todo_list.set_mode(mode)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.todo_new.resize(self.width(), self.height())
        self.todo_list.resize(self.width(), self.height())

    def deal_with_action(self, action, name):
        print('action :: ', action, ':', name)
        self.action_signal.emit(action, name)
