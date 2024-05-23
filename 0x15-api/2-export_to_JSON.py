#!/usr/bin/python3
# Script to analyze employee tasks using JSONPlaceholder API and write JSONfile

import requests
import sys
import json


if __name__ == "__main__":
    # Check if the script was called with an argument
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    # Get the employee ID from the command-line argument
    employee_id = int(sys.argv[1])
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
        employee_username = users[employee_id - 1]["username"]

        my_dict = {employee_id: []}

        for todo in todos:
            if todo["userId"] == employee_id:
                my_dict[employee_id].append({
                    "task": todo["title"],
                    "completed": todo["completed"],
                    "username": employee_username
                })

        with open('USER_ID.json', 'w', encoding="utf-8") as file:
            json.dump(my_dict, file)
    else:
        sys.exit(1)
