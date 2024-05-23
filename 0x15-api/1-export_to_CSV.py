#!/usr/bin/python3
# Script to analyze employee tasks using JSONPlaceholder API and write csv file

import requests
import sys
import csv


if __name__ == "__main__":
    # Check if the script was called with an argument
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    # Get the employee ID from the command-line argument
    employee_id = int(sys.argv[1])
    # API endpoint
    users_url = "https://jsonplaceholder.typicode.com/users/"

    # API endpoint
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

        with open('USER_ID.csv', 'w', newline="") as file:
            for todo in todos:
                if (todo["userId"]) == employee_id:
                    writer = csv.writer(file, quoting=csv.QUOTE_ALL)
                    writer.writerow([employee_id, employee_username,
                                     todo["completed"], todo["title"]])
    else:
        sys.exit(1)
