#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").__doc__)'
"""

import json
import requests


user_url = f'https://jsonplaceholder.typicode.com/users/'
todo_url = 'https://jsonplaceholder.typicode.com/todos/'


def run():
    """Main function"""
    user_response = requests.get(user_url)
    todo_response = requests.get(todo_url)

    # user_id = int(args[1])
    if user_response.status_code == 200:
        users = user_response.json()
        # print(users)
    else:
        print("Error:", f"Status code: {user_response.status_code}")

    if todo_response.status_code == 200:
        todos = todo_response.json()
        # users_todos = [todo for todo in todos if todo.get('userId') == user_id]
        # print(todos)
    else:
        print("Error:", f"Status code: {todo_response.status_code}")

    data_to_export = {}

    for user in users:
        tasks = []
        for task in todos:
            if user.get('id') == task.get('userId'):
                task_obj = {"username": f"{user.get('username')}",
                            "task": f"{task.get('title')}",
                            "completed": f"{task.get('completed')}"}
                tasks.append(task_obj)
        data_to_export[f'{user.get("id")}'] = tasks
    
    json_data = json.dumps(data_to_export)
    with open('todo_all_employees.json', "w") as file:
        file.write(json_data)


if __name__ == "__main__":
    run()
