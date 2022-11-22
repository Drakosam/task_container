from PySide6 import QtCore
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QWidget, QScrollArea, QVBoxLayout, QBoxLayout


class CustomScrollArea(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.list_item = []

        self.scroll_view = QScrollArea(self)
        self.frame = QWidget()
        self.layout = QVBoxLayout()

        self.layout.setDirection(QBoxLayout.TopToBottom)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        self.layout.setAlignment(Qt.AlignTop)
        self.frame.setLayout(self.layout)
        self.scroll_view.setWidget(self.frame)

        self.scroll_view.setWidgetResizable(True)
        self.scroll_view.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scroll_view.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

    def add_widget(self, widget):
        self.layout.addWidget(widget)
        self.list_item.append(widget)

    def clear(self):
        for item in self.list_item:
            self.layout.removeWidget(item)
            item.deleteLater()
        self.list_item.clear()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.scroll_view.setGeometry(0, 0, self.width(), self.height())
