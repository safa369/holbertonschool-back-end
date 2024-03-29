#!/usr/bin/python3
"""a script that returns information for a given employee."""

import json
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) > 1:
        id_emp = int(argv[1])
        url = 'https://jsonplaceholder.typicode.com/'
        request = requests.get('{}users/{}'.format(url, id_emp)).json()
        name = request.get('name')
        to_do = requests.get(url + "todos?userId={}".format(id_emp)).json()
        completed_tasks = []
        for task in to_do:
            task_info = {
                "username": name,
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            completed_tasks.append(task_info)
        data = {str(id_emp): completed_tasks}
        with open("todo_all_employees.json", "w") as json_file:
            json.dump(data, json_file, indent=4)
        print("Data exported to todo_all_employees.json successfully.")
