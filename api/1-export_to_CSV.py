#!/usr/bin/python3
"""a script that returns information for a given employee"""
from sys import argv
import csv
import requests

if __name__ == "__main__":
    if len(argv) > 1:
        id_emp = argv[1]
        url = 'https://jsonplaceholder.typicode.com/'
        req = requests.get('{}users/{}'.format(url, id_emp)).json()
        req_to_do = requests.get("{}todos?userID={}"
                                 .format(url, id_emp)).json()
        username = req.get("username")
        with open('{}.csv'.format(id_emp), 'w', newline='') as file:
            csv_data = csv.writer(file, delimiter=',', quoting=csv.QUOTE_ALL)
            for task in req_to_do:
                csv_data.writerow(["{}".format(id_emp),
                                   "{}".format(username),
                                   "{}".format(task.get("completed")),
                                   "{}".format(task.get("title"))])
