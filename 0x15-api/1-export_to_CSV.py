#!/usr/bin/python3
"""Restful API Module"""

import csv
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


def exportCsv(employee_id):
    """
    Function for exporting to csv

    Argument:
    employee_id (int): Id of the employee data to be fecthed

    """
    user_data, todo_data = get_employee_data(employee_id)

    userId = user_data.get('id')
    name = user_data.get('name')


    csvData = [
        [userId, name, task.get('completed'), task.get('title')]
        for task in todo_data
    ]

    # Define the CSV filename
    csv_filename = f'{userId}.csv'

    # Write to CSV file
    with open(csv_filename, mode='w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        csv_writer.writerows(csvData)

    print(f'Data exported to {csv_filename}')


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

    exportCsv(employee_id)
