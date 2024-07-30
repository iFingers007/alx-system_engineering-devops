#!/usr/bin/python3
"""Restful API Module"""

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
    todo_data = todo_response.json()

    return user_data, todo_data


def display_progress(employee_id):
    """
    Function for getting the id of the employee

    Argument:
    employee_id (int): Id of the employee data to be fecthed

    """
    user_data, todo_data = get_employee_data(employee_id)

    employee_name = user_data.get('name')

    # Filter tasks
    total_tasks = len(todo_data)
    done_tasks = [task for task in todo_data if task.get('completed')]

    # Get the number of completed tasks
    number_of_done_tasks = len(done_tasks)

    # Print the progress
    print(
        f'Employee {employee_name} is done with tasks
        ({number_of_done_tasks}/{total_tasks}):
        ')

    # Print the titles of the completed tasks
    for task in done_tasks:
        print(f'\t {task.get("title")}')


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

    display_todo_list_progress(employee_id)
