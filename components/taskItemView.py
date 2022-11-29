from PySide6 import QtCore
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QWidget, QPushButton


class TaskItemView(QWidget):
    action_signal = QtCore.Signal(str, int)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.buttonName = QPushButton(self)
        self.buttonMark = QPushButton(self)
        self.buttonDelete = QPushButton(self)

        self.buttonMark.setText('Stop')
        self.buttonDelete.setText('X')

        font_settings = QFont()
        font_settings.setBold(True)
        self.buttonName.setFont(font_settings)

        self.buttonName.clicked.connect(self._pick_item)
        self.buttonMark.clicked.connect(self._mark_item)
        self.buttonDelete.clicked.connect(self._delete_item)

        self.setMinimumHeight(35)

        self.item = None

    def set_name(self, item):
        self.item = item
        self.buttonName.setText(self.item.name)

        if self.item.status:
            self.buttonMark.setText('Start')
        else:
            self.buttonMark.setText('Stop')

    def _pick_item(self):
        self.action_signal.emit('pick', self.item.task_id)

    def _mark_item(self):
        self.action_signal.emit('mark', self.item.task_id)

    def _delete_item(self):
        self.action_signal.emit('delete', self.item.task_id)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.buttonName.setGeometry(0, 0, self.width() - 120, self.height())
        self.buttonMark.setGeometry(self.width() - 120, 0, 70, self.height())
        self.buttonDelete.setGeometry(self.width() - 50, 0, 50, self.height())
