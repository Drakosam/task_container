from PySide6 import QtCore
from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QFileDialog, QFrame, QLineEdit, QSpinBox


class AutoMoveView(QWidget):
    action_signal = QtCore.Signal(str, str)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.path_source = QLabel('xxx', self)
        self.path_target = QLabel('xxx', self)
        self.path_source.move(110, 0)
        self.path_target.move(110, 30)

        self.btt_source = QPushButton('Source', self)
        self.btt_source.clicked.connect(self.set_source)

        self.btt_target = QPushButton('Target', self)
        self.btt_target.clicked.connect(self.set_target)

        self.btt_update = QPushButton('Update', self)
        self.btt_update.clicked.connect(self.update)

        self.btt_source.resize(100, 30)
        self.btt_target.resize(100, 30)
        self.btt_target.move(0, 30)

        self.btt_update.move(0, 125)

        self.separator1 = QFrame(self)
        self.separator1.setFrameShape(QFrame.HLine)
        self.separator1.setFrameShadow(QFrame.Sunken)
        self.separator1.move(0, 60)

        self.label_1 = QLabel('Extension', self)
        self.label_1.move(20, 70)

        self.label_2 = QLabel('Cooldown (min)', self)
        self.label_2.move(20, 100)

        self.extension = QLineEdit(self)
        self.extension.resize(150, 30)
        self.extension.move(150, 60)

        self.cooldown = QSpinBox(self)
        self.cooldown.resize(150, 30)
        self.cooldown.move(150, 90)
        self.cooldown.setMinimum(1)

        self.path_source_selected = ''
        self.path_target_selected = ''

    def set_update(self):
        pass

    def set_source(self):
        path = QFileDialog.getExistingDirectory(self, 'Select Source Folder')
        self.path_source_selected = path
        self.path_source.setText(path)

    def set_target(self):
        path = QFileDialog.getExistingDirectory(self, 'Select Target Folder')
        self.path_target_selected = path
        self.path_target.setText(path)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.path_source.resize(self.width() - 110, 30)
        self.path_target.resize(self.width() - 110, 30)
        self.separator1.resize(self.width(), 2)
        self.btt_update.resize(self.width(), 30)
