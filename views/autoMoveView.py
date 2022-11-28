from functools import partial

from PySide6 import QtCore
from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QFileDialog, QFrame, QLineEdit, QSpinBox, QCheckBox

from components.customScrollArea import CustomScrollArea
from components.taskItemView import TaskItemView
from utylity import organizer
from utylity.signalNames import SignalNames


class AutoMoveView(QWidget):
    action_signal = QtCore.Signal(str, str)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.path_source = QLabel('xxx', self)
        self.path_target = QLabel('xxx', self)

        self.task_name = QLineEdit(self)
        self.task_name.setText('Task Name')

        self.btt_source = QPushButton('Source', self)
        self.btt_source.clicked.connect(self.set_source)

        self.btt_target = QPushButton('Target', self)
        self.btt_target.clicked.connect(self.set_target)

        self.btt_update = QPushButton('Update', self)
        self.btt_update.clicked.connect(self.update)

        self.btt_source.resize(100, 30)
        self.btt_target.resize(100, 30)

        self.btt_update.clicked.connect(self.update_item)

        self.separator1 = QFrame(self)
        self.separator1.setFrameShape(QFrame.HLine)
        self.separator1.setFrameShadow(QFrame.Sunken)

        self.label_1 = QLabel('Extension', self)

        self.label_2 = QLabel('Cooldown (min)', self)

        self.extension = QLineEdit(self)
        self.extension.setText('*.*')
        self.extension.resize(150, 30)

        self.cooldown = QSpinBox(self)
        self.cooldown.resize(150, 30)
        self.cooldown.setMinimum(1)

        self.check_box = QCheckBox('Done', self)

        self.label_3 = QLabel('Active Tasks', self)
        self.label_4 = QLabel('Dormant Tasks', self)

        self.task_name.move(5, 0)
        self.path_source.move(110, 30)
        self.btt_source.move(5, 30)
        self.path_target.move(110, 60)
        self.btt_target.move(5, 60)
        self.separator1.move(0, 90)
        self.extension.move(150, 90)
        self.cooldown.move(150, 120)
        self.label_1.move(20, 100)
        self.label_2.move(20, 130)
        self.check_box.move(20, 155)
        self.btt_update.move(5, 185)
        self.label_3.move(5, 220)
        self.label_4.move(5, 220)

        self.task_id = 0

        self.active_task = CustomScrollArea(self)
        self.dormant_task = CustomScrollArea(self)


    def update_item(self):
        print('update auto move')
        print()
        organizer.update_auto_move_item(
            task_id=self.task_id,
            name=self.task_name.text(),
            source=self.path_source.text(),
            target=self.path_target.text(),
            extension=self.extension.text(),
            cooldown=self.cooldown.value(),
            status=self.check_box.isChecked()
        )

        if self.task_id == 0:
            self.task_id = 0
            self.task_name.setText('Task Name')
            self.path_source.setText('xxx')
            self.path_target.setText('xxx')
            self.extension.setText('*.*')
            self.cooldown.setValue(1)
            self.check_box.setChecked(False)

        self.action_signal.emit('auto_move_items', SignalNames.ITEM_UPDATE.value)

    def set_source(self):
        path = QFileDialog.getExistingDirectory(self, 'Select Source Folder')
        self.path_source.setText(path)

    def set_target(self):
        path = QFileDialog.getExistingDirectory(self, 'Select Target Folder')
        self.path_target.setText(path)

    def update_view(self):
        self.active_task.clear()
        self.dormant_task.clear()
        for item in organizer.auto_move:

            btt = TaskItemView()
            btt.set_name(item)
            btt.setMinimumHeight(30)
            btt.action_signal.connect(self.deal_with_signal)
            if not item.status:
                self.active_task.add_widget(btt)
            else:
                self.dormant_task.add_widget(btt)

    def set_item(self, item):
        self.task_id = item.task_id
        self.task_name.setText(item.name)
        self.path_source.setText(item.source_path)
        self.path_target.setText(item.target_path)
        self.extension.setText(item.extension)
        self.cooldown.setValue(item.cooldown)
        self.check_box.setChecked(item.status)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.task_name.resize(self.width() - 10, 30)
        self.path_source.resize(self.width() - 110, 30)
        self.path_target.resize(self.width() - 110, 30)
        self.separator1.resize(self.width(), 2)
        self.btt_update.resize(self.width() - 10, 30)

        self.active_task.resize(int(self.width() / 2) - 10, self.height() - 250)
        self.active_task.move(5, 250)
        self.dormant_task.resize(int(self.width() / 2) - 10, self.height() - 250)
        self.dormant_task.move(int(self.width() / 2), 250)
        self.label_4.move(int(self.width() / 2), 220)

    def deal_with_signal(self, signal_name, item_id):
        if signal_name == 'pick':
            success, item = organizer.get_auto_move_item(item_id)
            if success:
                self.set_item(item)
        if signal_name == 'mark':
            success, item = organizer.get_auto_move_item(item_id)
            if success:
                item.status = not item.status
            self.set_item(item)
        if signal_name == 'delete':
            organizer.remove_auto_move_item(item_id)
        self.update_view()
