import sys
import os
from datetime import datetime
import uuid
import json

# project_name = sys.argv[1]
# project_id = sys.argv[2]
project_name = 'Some Application'
project_id = 'f6b618af-6e82-4f7b-b096-dc5ab0999f53'
now = datetime.now()
today = f'{now.day}/{now.month}/{now.year}'

username = os.getlogin()
app_data_path = f'C:\\Users\\{username}\\AppData\\Local\\bugr'
app_data = os.listdir(app_data_path)


def find_file(data, path):
    for obj in data:
        object_path = f'{path}\\{obj}'
        if os.path.isdir(object_path):
            contents = os.listdir(object_path)
            return find_file(contents, object_path)
        else:
            with open(object_path, 'r+') as data_file:
                json_data = data_file.read()
                data_dict = json.loads(json_data)
                if data_dict['project_id'] == project_id:
                    return object_path


file_path = find_file(app_data, app_data_path)

with open(file_path, 'r') as file:
    original_data = file.read()
    original_data_dict = json.loads(original_data)
    original_data_dict['groups'].append({
        'title': 'New Group',
        'group_id': str(uuid.uuid4()),
        'created_at': str(now),
        'issues': [{
            'description': f'{project_name} Issue',
            'issue_id': str(uuid.uuid4()),
            'created_at': str(now),
            'last_modified': str(now),
            'finish_by': str(today),
            'priority': 'Low',
            'stage': 'Todo'
        }]
    })

with open(file_path, 'w+') as new_file:
    new_json_data = json.dumps(original_data_dict)
    new_file.write(new_json_data)
