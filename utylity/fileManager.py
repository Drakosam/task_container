import json
from os.path import exists

from utylity import organizer


def save_to_file():
    notes = ','.join([str(x) for x in organizer.notes])
    todos = ','.join([str(x) for x in organizer.todos])
    auto_items = ','.join([str(x) for x in organizer.auto_move])

    data = '{"notes":[' + notes + '],"todos":[' + todos + '], "auto_items":[' + auto_items + ']}'
    print(data)

    with open('data.json', 'w') as file:
        file.write(data)


def load_from_file():
    if not exists('data.json'):
        return {}

    with open('data.json', 'r') as file:
        data = json.load(file)

        if 'notes' in data:
            for note in data['notes']:
                organizer.add_note_from_json(note)
            organizer.category_list = organizer.get_notes_categories()

        if 'todos' in data:
            for todo in data['todos']:
                organizer.add_todo_from_json(todo)

        if 'auto_items' in data:
            for auto_item in data['auto_items']:
                organizer.add_auto_move_from_jason(auto_item)