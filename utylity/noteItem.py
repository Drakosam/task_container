from typing import List


class Note:
    def __init__(self, name: str = '', content: str = '', note_id: int = 0, category_name: str = ''):
        self.name = name
        self.content = content
        self.category_name = category_name
        self.note_id = note_id

    def __str__(self):
        body = f'"name":{self.name}'
        body += f',"content":{self.content}'
        body += f',"category_name":{self.category_name}'
        body += f',"note_id":{self.note_id}'

        return '{' + body + '}'
