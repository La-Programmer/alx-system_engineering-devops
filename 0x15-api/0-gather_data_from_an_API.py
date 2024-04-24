#!/usr/bin/python3
"""This module makes a GET request to an API for user and tasks
"""

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
        # print(response)
        data = user_response.json()
        # print("Response data: ", data)
    else:
        print("Error:", f"Status code: {user_response.status_code}")

    if todo_response.status_code == 200:
        # print(todo_response)
        todo_list = todo_response.json()
        user_todo_list = [
                            todo for todo in todo_list
                            if todo.get('userId') == user_id]
        # print("Todo List: ", todo_list)
        completed_tasks = []
        nt = len(user_todo_list)
        for task in user_todo_list:
            if task.get('completed') is True:
                completed_tasks.append(task)
        # print("User's todo list: ", user_todo_list)
        ct = len(completed_tasks)
        print(
            f"Employee {data.get('name')} is done with tasks({ct}/{nt}):")
        for task in completed_tasks:
            print(f"\t {task.get('title')}")
    else:
        print("Error:", f"Status code: {todo_response.status_code}")


if __name__ == "__main__":
    run()
