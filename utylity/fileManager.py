import json
from os.path import exists

from utylity import organizer


def save_to_file():
    notes = ','.join([str(x) for x in organizer.notes])
    data = '{"notes":[' + notes + ']}'
    with open('data.json', 'w') as file:
        file.write(data)


def load_from_file():
    if not exists('data.json'):
        return {}

    with open('data.json', 'r') as file:
        data = json.load(file)
        for note in data['notes']:
            organizer.add_note_from_json(note)
