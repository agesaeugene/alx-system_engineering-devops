#!/usr/bin/python3
"""
exports every employee's to-do list data in JSON format.

This script exports the data to a JSON file after retrieving each 
employee's user details and to-do lists from the JSONPlaceholder API.

"""
import json
import requests


def fetch_user_data():
    """Fetch user information and to-do lists for all employees."""

    url = "https://jsonplaceholder.typicode.com/"

    users = requests.get(url + "users").json()

    data_to_export = {}
    for user in users:
        user_id = user["id"]
        user_url = url + f"todos?userId={user_id}"
        todo_list = requests.get(user_url).json()

        data_to_export[user_id] = [
            {
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": user.get("username"),
            }
            for todo in todo_list
        ]

    return data_to_export


if __name__ == "__main__":
    data_to_export = fetch_user_data()


    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(data_to_export, jsonfile, indent=4)

