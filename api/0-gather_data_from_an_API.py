#!/usr/bin/python3
"""a script that returns information about a given employee"""

import requests
from sys import argv


if __name__ == "__main__":
    """Show information about employee"""
    if len(argv) > 1:
        id_emp = int(argv[1])
        url = "https://jsonplaceholder.typicode.com/"
        req = requests.get("{}users/{}".format(url, id_emp))
        name_e = req.json().get("name")
        if name_e is not None:
            req_to_do = requests.get("{}todos?userID={}"
                                     .format(url, id_emp)).json()
            all_tasks = len(req_to_do)
            completed_task = []
            count = 0
            for t_c in req_to_do:
                if t_c.get("completed") is True:
                    completed_task.append(t_c)
                    count += 1
            print("Employee {} is done with tasks({} / {}):"
                  .format(name_e, count, all_tasks))
            for t in completed_task:
                print("\t {}".format(t.get("title")))
