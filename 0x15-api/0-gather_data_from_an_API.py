#!/usr/bin/python3
"""Analyzes employee tasks (completed/total) using JSONPlaceholder API"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    users_url = "https://jsonplaceholder.typicode.com/users/"
    todos_url = "https://jsonplaceholder.typicode.com/todos/"
    todos_res = requests.get(todos_url)
    users_res = requests.get(users_url)

    if todos_res.status_code == 200 and users_res.status_code == 200:
        todos = todos_res.json()
        users = users_res.json()
        employee_name = users[employee_id - 1]["name"]
        count_completed = 0
        count_all_tasks = 0
        tasks_completed = []

        for todo in todos:
            if (todo["userId"]) == employee_id:
                count_all_tasks += 1
                if (todo["completed"]):
                    count_completed += 1
                    tasks_completed.append(todo["title"])
    print("Employee {} is done with tasks({}/{}):".
          format(employee_name, count_completed, count_all_tasks))
    for task in tasks_completed:
        print("\t {}".format(task))
    else:
        sys.exit(1)
