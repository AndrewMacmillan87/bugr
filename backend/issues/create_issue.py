import sys
import os
from datetime import datetime
import uuid
import json


def find_file(path, project_id):
    for (root, dirs, files) in os.walk(path, topdown=False):
        for file in files:
            with open(f'{root}/{file}', 'r') as project_file:
                json_data = project_file.read()
                data_dict = json.loads(json_data)
                if data_dict['project_id'] == project_id:
                    return f'{root}/{file}'


def main():
    username = os.getlogin()
    project_name = sys.argv[1]
    project_id = sys.argv[2]
    group_id = sys.argv[3]
    now = datetime.now()
    today = f'{now.day}/{now.month}/{now.year}'
    file_path = find_file(f'C:\\Users\\{username}\\AppData\\Local\\bugr', project_id)

    with open(file_path, 'r') as file:
        original_data = file.read()
        original_data_dict = json.loads(original_data)
        groups = original_data_dict['groups']
        for group in groups:
            if group['group_id'] == group_id:
                group['issues'].append({
                    "description": f"{project_name} Issue",
                    "issue_id": str(uuid.uuid4()),
                    "created_at": str(now),
                    "last_modified": str(now),
                    "finish_by": str(today),
                    "priority": "Low",
                    "stage": "Todo"
                })

    with open(file_path, 'w+') as new_file:
        new_json_data = json.dumps(original_data_dict)
        new_file.write(new_json_data)

    print(json.dumps(original_data_dict))


if __name__ == "__main__":
    main()
