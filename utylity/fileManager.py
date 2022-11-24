import json
from os.path import exists

from utylity import organizer


def save_to_file():
    notes = ','.join([str(x) for x in organizer.notes])
    todos = ','.join([str(x) for x in organizer.todos])

    data = '{"notes":[' + notes + '],"todos":[' + todos + ']}'

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

        if 'todos' in data:
            for todo in data['todos']:
                organizer.add_todo_from_json(todo)
