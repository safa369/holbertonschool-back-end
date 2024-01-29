#!/usr/bin/python3
"""a script that returns information for a given employee."""

import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) > 1:
        id_emp = argv[1]
        url = 'https://jsonplaceholder.typicode.com/'
        req = requests.get('{}users/{}'.format(url, id_emp)).json()
        name_e = req.get("name")
        if name_e is not None:
            req_to_do = requests.get("{}TODOS?userID={}"
                                     .format(url, id_emp)).json()
            all_tasks = len(req_to_do.get("task"))
            completed_task = [t_c for t_c in req_to_do
                              if t_c.get("completed") is True]
            count = len(completed_task)
            print("Employee {} is done with tasks({}/{}):"
                  .format(name_e, count, all_tasks))
            for t in completed_task:
                print("\t {}".format(t.get("title")))
