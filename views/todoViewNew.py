from PySide6.QtWidgets import QWidget, QLabel


class ToDoViewNew(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        label = QLabel("To Do New", self)