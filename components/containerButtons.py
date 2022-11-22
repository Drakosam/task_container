from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QPushButton

from utylity.signalNames import SignalNames


class ContainerButton(QWidget):
    pick_signal = Signal(str, str)

    def __init__(self, container_name, **kwargs):
        super().__init__(**kwargs)
        self.children_items = []
        self.expand = False
        self.main_button = QPushButton(container_name, self)
        self.main_button.pressed.connect(self.on_press)
        self.setFixedHeight(40)

    def on_press(self):
        self.expand = not self.expand
        self.expand_proc()
        if self.expand:
            self.pick_signal.emit(SignalNames.LOCAL_UPDATE.value, self.main_button.text())
        else:
            self.pick_signal.emit(SignalNames.LOCAL_UPDATE.value, '')

    def add_child(self, child_name):
        child_button = QPushButton(child_name, self)
        child_button.move(10, 40 + 40 * len(self.children_items))
        child_button.resize(self.width() - 10, 40)
        self.children_items.append(child_button)
        child_button.pressed.connect(lambda: self.pick_signal.emit(SignalNames.GLOBAL_UPDATE.value, child_name))
        self.expand_proc()

    def expand_proc(self):
        if self.expand:
            self.setFixedHeight(40 + 40 * len(self.children_items))

        else:
            self.setFixedHeight(40)

    def resizeEvent(self, event):
        self.main_button.resize(self.width(), 40)
        for child in self.children_items:
            child.resize(self.width() - 10, 40)
