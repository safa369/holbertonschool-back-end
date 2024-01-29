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
        completed_task = []
        for task in to_do:
            if task.get('completed') is True:
                completed_task.append(task)
        count = len(completed_task)
        print("Employee {} is done with tasks({}/{}):"
              .format(name, count, len(to_do)))
        for t in completed_task:
            print("\t {}".format(t.get("title")))
