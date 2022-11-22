from typing import List


class Note:
    def __init__(self, name: str = '', content: str = '', note_id: int = 0):
        self.name = name
        self.content = content
        self.note_id = note_id

    def __str__(self):
        return '{' + f'"name":"{self.name}", "content":"{self.content}", "note_id":"{self.note_id}"' + '}'


class NoteContainer:
    def __init__(self, category_name: str):
        self.category_name = category_name
        self.notes: List[Note] = []

    def find_next_note_id(self):
        return [x.note_id for x in self.notes]

    def add_note(self, note_name, content, note_id):
        print(f'add_note: {note_name}, {content}, {note_id}')
        if note_id not in self.find_next_note_id():
            return self._add_new_note_process(note_name, content, note_id)
        else:
            return self._update_note_process(note_name, content, note_id)

    def _add_new_note_process(self, note_name, content, note_id=0):
        self.notes.append(Note(note_name, content, note_id))
        return True

    def _update_note_process(self, note_name, content, note_id=0):
        for note in self.notes:
            if note.note_id == note_id:
                note.name = note_name
                note.content = content
                return True
        return self._add_new_note_process(note_name, content)

    def __str__(self):
        content = f'"notes":[{",".join([str(x) for x in self.notes])}]'
        return '{' + f'"category_name":"{self.category_name}", {content}' + '}'
