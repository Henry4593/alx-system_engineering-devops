#!/usr/bin/python3
# Script to analyze employee tasks using JSONPlaceholder API and write JSONfile

import requests
import sys
import json


if __name__ == "__main__":
    # API endpoint
    users_url = "https://jsonplaceholder.typicode.com/users/"
    todos_url = "https://jsonplaceholder.typicode.com/todos/"

    # Make the request
    todos_res = requests.get(todos_url)
    users_res = requests.get(users_url)

    # Check if the request was successful
    if todos_res.status_code == 200 and users_res.status_code == 200:
        # Parse the JSON data
        todos = todos_res.json()
        users = users_res.json()

        my_dict = {}

        for user in users:
            employee_id = user["id"]
            employee_username = user["username"]
            my_dict[employee_id] = []

            for todo in todos:
                if todo["userId"] == employee_id:
                    my_dict[employee_id].append({
                        "username": employee_username,
                        "task": todo["title"],
                        "completed": todo["completed"]
                    })

        with open('todo_all_employees.json', 'w', encoding="utf-8") as file:
            json.dump(my_dict, file)
    else:
        sys.exit(1)
