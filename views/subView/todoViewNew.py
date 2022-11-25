from PySide6 import QtCore
from PySide6.QtWidgets import QWidget, QLineEdit, QTextEdit, QPushButton

from utylity import organizer
from utylity.signalNames import SignalNames


class ToDoViewNew(QWidget):
    action_signal = QtCore.Signal(str, str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.todo_name = QLineEdit(self)
        self.todo_content = QTextEdit(self)
        self.todo_btt = QPushButton(self)

        self.todo_name.move(5, 5)
        self.todo_content.move(5, 35)

        self.todo_btt.setText('Add New Item')
        self.todo_btt.clicked.connect(self.add_new_item)

    def add_new_item(self):
        status, _ = organizer.update_todo(self.todo_name.text(), self.todo_content.toPlainText())

        if status:
            self.action_signal.emit('todo', SignalNames.ITEM_UPDATE)

        self.todo_name.setText('')
        self.todo_content.setText('')

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.todo_name.resize(self.width() - 10, 30)
        self.todo_content.resize(self.width() - 10, self.height() - 40)
        self.todo_btt.resize(self.width() - 10, 30)
        self.todo_btt.move(5, self.height() - 35)
