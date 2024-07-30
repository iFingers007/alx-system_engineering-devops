#!/usr/bin/python3
"""Restful API Module"""

import json
import requests
import sys


def getAll():
    """
    Function for getting all data
    """
    base_url = 'https://jsonplaceholder.typicode.com/'
    user_response = requests.get(f'{base_url}users')
    user_data = user_response.json()

    todo_resp = requests.get(f'{base_url}todos')
    todo_data = todo_resp.json()

    return user_data, todo_data


def exportAll():
    """
    Function for exporting to csv
    """
    user_data, todo_data = getAll()

    jsonData = {}

    for users in user_data:
        user_id = str(users.get('id'))
        username = users.get('username')

        user_task = [
            {
                "username": username,
                "task": task.get('title'),
                "completed": task.get('completed')
            }
            for task in todo_data if task.get('userId') == users.get('id')
        ]

        jsonData[user_id] = user_task

    # Define the Json filename

    json_filename = 'todo_all_employees.json'

    # Write to Json file
    with open(json_filename, mode='w') as jsonFile:
        json.dump(jsonData, jsonFile)


if __name__ == '__main__':
    exportAll()
