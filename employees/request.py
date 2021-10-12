EMPLOYEES = [
    {
        "id": 1,
        "name": "Joe",
        "locationId": 1
    },
    {
        "id": 2,
        "name": "Rosa",
        "locationId": 1
    },
    {
        "id": 3,
        "name": "Nick",
        "locationId": 2
    }
]


def get_all_employees():
    '''Returns all employees'''
    return EMPLOYEES


def get_single_employee(id):
    # Variable to hold the found employee, if it exists
    requested_employee = None

    # Iterate the EMPLOYEE list above. Very similar to the
    # for..of loops you used in JavaScript.
    for employee in EMPLOYEES:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee


def create_employee(employee):
    # Get the id value of the last employee in the list
    max_id = EMPLOYEES[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the employee dictionary
    employee["id"] = new_id

    # Add the employee dictionary to the list
    EMPLOYEES.append(employee)

    # Return the dictionary with `id` property added
    return employee


def delete_employee(id):
    # Initial -1 value for customer index, in case one isn't found
    employee_index = -1
    
    # This loops through employees.
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            # If employee id is found, store the index.
            employee_index = index

    # If the customer is found, remove it from the list.
    if employee_index >= 0:
        EMPLOYEES.pop(employee_index)