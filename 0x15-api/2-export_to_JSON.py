#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").__doc__)'
"""

import json
import requests
import sys

args = sys.argv

user_url = f'https://jsonplaceholder.typicode.com/users/{args[1]}'
todo_url = 'https://jsonplaceholder.typicode.com/todos/'


def run():
    """Main function"""
    user_response = requests.get(user_url)
    todo_response = requests.get(todo_url)

    user_id = int(args[1])
    if user_response.status_code == 200:
        data = user_response.json()
    else:
        print("Error:", f"Status code: {user_response.status_code}")

    if todo_response.status_code == 200:
        todos = todo_response.json()
        users_todos = [todo for todo in todos if todo.get('userId') == user_id]
        # print(users_todos)
    else:
        print("Error:", f"Status code: {todo_response.status_code}")

    data_to_export = {}
    task = []

    for todo in users_todos:
        todo_obj = {"task": f"{todo.get('title')}",
                    "completed": f"{todo.get('completed')}",
                    "username": f"{data.get('username')}"}
        task.append(todo_obj)
    data_to_export[args[1]] = task
    # print(data_to_export)
    json_data = json.dumps(data_to_export)
    # print(json_data)
    with open(f"{args[1]}.json", "w") as file:
        file.write(json_data)


if __name__ == "__main__":
    run()
