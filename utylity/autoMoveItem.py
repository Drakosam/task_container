import os
from datetime import datetime


class AutoMoveItem:
    def __init__(self, task_id=0, name='', source_path='', target_path='', extension='', cooldown=1, status=False):
        self.task_id = task_id
        self.name = name
        self.source_path = source_path
        self.target_path = target_path
        self.extension = extension
        self.cooldown = cooldown
        self.status = status
        self.next_run = self.cooldown

    def __str__(self):
        item = f'"name": "{self.name}"'
        item += f', "task_id": {self.task_id}'
        item += f', "source_path": "{self.source_path}"'
        item += f', "target_path": "{self.target_path}"'
        item += f', "extension": "{self.extension}"'
        item += f', "cooldown": {self.cooldown}'
        item += f', "status": {"true" if self.status else "false"}'

        return '{' + item + '}'

    def is_next_run_time(self):
        self.next_run -= 1
        if self.next_run <= 0:
            self.next_run = self.cooldown
            return True
        return False

    def execute(self):
        print(f'Executing {self.name}')
        if not os.path.exists(self.target_path):
            return False

        for file in os.listdir(self.source_path):
            if file.endswith(self.extension):
                if not os.path.exists(self.target_path + '\\' + file):
                    os.rename(self.source_path + '\\' + file, self.target_path + '\\' + file)
                else:
                    os.rename(f'{self.source_path}/{file}',
                              f'{self.target_path}/{datetime.timestamp(datetime.now())}_{file}')
