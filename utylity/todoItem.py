class ToDoItem(object):
    def __init__(self, name='', description='', item_id=0, active=True):
        self.name = name
        self.description = description
        self.item_id = item_id
        self.active = active

    def __str__(self):
        body = f'"name":"{self.name}","description":"{self.description}","id":{self.item_id}'
        body += f',"active":{"true" if self.active else "false"}'
        return '{' + body + '}'
