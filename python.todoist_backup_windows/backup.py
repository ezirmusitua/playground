import json
import sys
import todoist

from os import path
from datetime import datetime

token = sys.argv[1]
backup_dir = sys.argv[2]

DUMP_FIELDS = [
    'activity',
    'backups',
    'biz_invitations',
    'business_users',
    'collaborators',
    'collaborator_states',
    'completed',
    'emails',
    'filters',
    'invitations',
    'items',
    'labels',
    'live_notifications',
    'locations',
    'notes',
    'projects',
    'project_notes',
    'quick',
    'reminders',
    'templates',
    'user',
]

to_dump = dict()

for f in DUMP_FIELDS:
    to_dump[f] = []

api = todoist.TodoistAPI(sys.argv[1])

api.sync()

for f in DUMP_FIELDS:
    if isinstance(api.state.get(f, []), list):
        for i in api.state.get(f, []):
            try:
                to_dump[f].append(i.data)
            except Exception as e:
                to_dump[f].append(i)
    else:
        item = api.state.get(f)
        to_dump[f].append(item)

with open(path.join(backup_dir, datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '.json'), 'w') as wf:
    json.dump(to_dump, wf)
