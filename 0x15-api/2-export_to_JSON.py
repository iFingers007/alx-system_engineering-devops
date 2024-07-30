#!/usr/bin/python3
"""Restful API Module"""

import json
import requests
import sys


def get_employee_data(employee_id):
    """Function for getting the id of the employee

    Argument:
    employee_id (int): Id of the employee data to be fecthed

    """
    base_url = 'https://jsonplaceholder.typicode.com/'
    user_response = requests.get(f'{base_url}users/{employee_id}')
    user_data = user_response.json()

    todo_resp = requests.get(f'{base_url}todos?userId={employee_id}')
    todo_data = todo_resp.json()

    return user_data, todo_data


def exportJson(employee_id):
    """
    Function for exporting to csv

    Argument:
    employee_id (int): Id of the employee data to be fecthed

    """
    user_data, todo_data = get_employee_data(employee_id)

    userId = user_data.get('id')
    name = user_data.get('username')


    jsonData = {
        userId: [
            {
                "task": task.get('title'),
                "completed": task.get('completed'),
                "name":name
            }
            for task in todo_data
        ]
    }

    # Define the Json filename
    json_filename = f'{userId}.json'

    # Write to Json file
    with open(json_filename, mode='w', newline='') as jsonFile:
        json.dump(jsonData, jsonFile, indent=4)

    print(f'Data exported to {json_filename}')


if __name__ == '__main__':
    # Ensure an employee ID is provided
    if len(sys.argv) != 2:
        print('Usage: python3 script.py <employee_id>')
        sys.exit(1)

    # Get the employee ID from the command line arguments
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print('Please provide a valid employee ID (integer).')
        sys.exit(1)

    exportJson(employee_id)
