#!/usr/bin/python3
"""This module exports to a CSV file"""

import csv
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
        print(users_todos)
    else:
        print("Error:", f"Status code: {todo_response.status_code}")

    data_to_export = []
    for todo in users_todos:
        task = [
                f'{todo.get("userId")}',
                f'{data.get("username")}',
                f'{todo.get("completed")}',
                f'{todo.get("title")}']
        data_to_export.append(task)
    print(data_to_export)

    with open(f"{user_id}.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data_to_export)


if __name__ == "__main__":
    run()
