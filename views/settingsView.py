from PySide6.QtWidgets import QWidget, QLabel


class SettingsView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        label = QLabel("Settings", self)