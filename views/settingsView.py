from PySide6 import QtCore
from PySide6.QtWidgets import QWidget, QLabel


class SettingsView(QWidget):
    action_signal = QtCore.Signal(str, str)

    def __init__(self, parent=None):
        super().__init__(parent)
        label = QLabel("Settings", self)
