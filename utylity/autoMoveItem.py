class AutoMoveItem:
    def __init__(self, task_id=0, name='', source_path='', target_path='', extension='', cooldown=1, status=False):
        self.task_id = task_id
        self.name = name
        self.source_path = source_path
        self.target_path = target_path
        self.extension = extension
        self.cooldown = cooldown
        self.status = status

    def __str__(self):
        item = f'"name": "{self.name}"'
        item += f', "task_id": "{self.task_id}"'
        item += f', "source_path": "{self.source_path}"'
        item += f', "target_path": "{self.target_path}"'
        item += f', "extension": "{self.extension}"'
        item += f', "cooldown": {self.cooldown}'
        item += f', "status": {"true" if self.status else "false"}'

        return '{' + item + '}'
