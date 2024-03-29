#!/usr/bin/python3
"""a script that returns information for all employees."""

import json
import requests


def fetch_user_tasks(user_id):
    url = 'https://jsonplaceholder.typicode.com/'
    user_data = requests.get('{}users/{}'.format(url, user_id)).json()
    username = user_data.get('username')
    tasks = requests.get(url + "todos?userId={}".format(user_id)).json()
    completed_tasks = []
    for task in tasks:
        task_info = {
            "username": username,
            "task": task.get("title"),
            "completed": task.get("completed")
        }
        completed_tasks.append(task_info)
    return completed_tasks


if __name__ == "__main__":
    all_user_tasks = {}
    for user_id in range(1, 11):  # Assuming users are from id 1 to 10
        all_user_tasks[str(user_id)] = fetch_user_tasks(user_id)

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_user_tasks, json_file, indent=4)
