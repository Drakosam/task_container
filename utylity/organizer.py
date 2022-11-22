from typing import List

from utylity.noteItem import NoteContainer, Note


class Organizer:
    def __init__(self):
        self.notes: List[NoteContainer] = []

    def add_notes_new_category(self, category_name: str):
        if category_name in self.get_notes_categories():
            return False
        self.notes.append(NoteContainer(category_name))
        return True

    def get_notes_categories(self):
        return [x.category_name for x in self.notes]

    def add_note_from_json(self, note: dict):
        category_name = note['category_name']
        self.add_notes_new_category(category_name)

        for note in note['notes']:
            self.update_note_content(category_name, note['name'], note['content'], note['note_id'])

    def remove_notes_category(self, name):
        if name not in self.get_notes_categories():
            return False
        self.notes = [x for x in self.notes if x.category_name != name]

    def update_note_content(self, category_name, note_name, content, note_id=0):
        print(f'update_note_content: {category_name}, {note_name}, {content}, {note_id}')

        if category_name not in self.get_notes_categories():
            return False, note_id

        if note_name == '':
            return False, note_id

        if note_id == 0:
            note_id = self.find_next_note_id()

        print(f'note_id: {note_id}')
        note_category = None

        for note in self.notes:
            if note.category_name == category_name:
                note_category = note
                break

        return note_category.add_note(note_name, content, note_id), note_id

    def delete_note_content(self, category_name, note_id=0):
        if category_name not in self.get_notes_categories():
            return False

        for note in self.notes:
            if note.category_name == category_name:
                note.notes = [x for x in note.notes if x.note_id != note_id]
                return True
        return False

    def get_notes_from_category(self, category_name):
        for category in self.notes:
            if category.category_name == category_name:
                return category.notes
        return []

    def get_note(self, note_category, note_id):
        for note in self.notes:
            if note.category_name == note_category:
                for note in note.notes:
                    if note.note_id == note_id:
                        return note
        return Note()

    def find_next_note_id(self):
        notes_ids = []
        for note in self.notes:
            notes_ids += note.find_next_note_id()

        print(f'notes_ids: {notes_ids}')
        if len(notes_ids) == 0:
            return 1
        return max(notes_ids) + 1
