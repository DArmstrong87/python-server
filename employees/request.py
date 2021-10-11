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
