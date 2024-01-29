#!/usr/bin/python3
"""a script that returns information for a given employeein JSON format"""
import json
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        id_emp = sys.argv[1]
        url = 'https://jsonplaceholder.typicode.com/'
        req = requests.get(url + 'users/{}'.format(id_emp)).json()
        name_e = req.get("name")
        username = req.get("username")
        req_to_do = requests.get(url + "todos?userID={}"
                                 .format(id_emp)).json()
        all_tasks = len(req_to_do)
        with open('{}.json'.format(id_emp), 'w') as file:
            json.dump({id_emp: [{
                "task": (t_c.get("title")),
                "completed": (t_c.get("completed")),
                "username": username}
                for t_c in req_to_do]}, file)
