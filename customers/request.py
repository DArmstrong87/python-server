import sqlite3
import json
from models import Customer

CUSTOMERS = [
    {
        "id": 1,
        "name": "Jessica Younker",
        "email": "jessica@younker.com",
        "employee": True
    },
    {
        "id": 2,
        "name": "Jordan Nelson",
        "email": "jordan@nelson.com",
        "employee": True
    },
    {
        "id": 3,
        "name": "Zoe LeBlanc",
        "email": "zoe@leblanc.com",
        "employee": True
    },
    {
        "name": "Meg Ducharme",
        "email": "meg@ducharme.com",
        "id": 4,
        "employee": True
    },
    {
        "name": "Hannah Hall",
        "email": "hannah@hall.com",
        "id": 5,
        "employee": True
    },
    {
        "name": "Emily Lemmon",
        "email": "emily@lemmon.com",
        "id": 6,
        "employee": True
    },
    {
        "name": "Jordan Castelloe",
        "email": "jordan@castelloe.com",
        "id": 7,
        "employee": True
    },
    {
        "name": "Leah Gwin",
        "email": "leah@gwin.com",
        "id": 8,
        "employee": True
    },
    {
        "name": "Caitlin Stein",
        "email": "caitlin@stein.com",
        "id": 9,
        "employee": True
    },
    {
        "name": "Greg Korte",
        "email": "greg@korte.com",
        "id": 10,
        "employee": True
    },
    {
        "name": "Charisse Lambert",
        "email": "charisse@lambert.com",
        "id": 11,
        "employee": True
    },
    {
        "name": "Madi Peper",
        "email": "madi@peper.com",
        "id": 12,
        "employee": True
    },
    {
        "id": 15,
        "name": "Ryan Tanay",
        "email": "ryan@tanay.com",
        "employee": False
    },
    {
        "id": 16,
        "name": "Emma Beaton",
        "email": "emma@beaton.com",
        "employee": False
    },
    {
        "id": 17,
        "name": "Dani Adkins",
        "email": "dani.adkins.com",
        "employee": False
    },
    {
        "id": 18,
        "name": "Adam Oswalt",
        "email": "adam@oswalt.com",
        "employee": False
    },
    {
        "id": 19,
        "name": "Fletcher Bangs",
        "email": "flangs@bangs.com",
        "employee": False
    },
    {
        "id": 20,
        "name": "Angela Lee",
        "email": "lee@lee.com",
        "employee": False
    },
    {
        "name": "mike mike",
        "email": "m@m.com",
        "employee": False,
        "id": 21
    },
    {
        "name": "Eric \"Macho Man\" Taylor",
        "email": "macho@man.com",
        "employee": True,
        "id": 22
    }
]


def get_all_customers():
    # Open a connection to the database
    with sqlite3.connect("./kennel.db") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address,
            a.employee,
            a.email,
            a.password
        FROM customer a
        """)

        # Initialize an empty list to hold all animal representations
        customers = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an animal instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Animal class above.
            customer = Customer(
                row['id'], row['name'], row['address'], row['employee'], row['email'], row['password'])

            customers.append(customer.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(customers)


def get_single_customer(id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address,
            a.email,
            a.password
        FROM customer a
        WHERE a.id = ?
        """, (id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an customer instance from the current row
        customer = Customer(data['id'], data['name'],
                            data['address'], data['email'], data['password'])

        return json.dumps(customer.__dict__)


def create_customer(customer):
    # Get the id value of the last customer in the list
    max_id = CUSTOMERS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the customer dictionary
    customer["id"] = new_id

    # Add the customer dictionary to the list
    CUSTOMERS.append(customer)

    # Return the dictionary with `id` property added
    return customer


def delete_customer(id):
    # Initial -1 value for customer index, in case one isn't found
    customer_index = -1

    # Iterate the CUSTOMERS list, but use enumerate() so that you
    # can access the index value of each item
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            # Found the customer. Store the current index.
            customer_index = index

    # If the customer was found, use pop(int) to remove it from list
    if customer_index >= 0:
        CUSTOMERS.pop(customer_index)


def update_customer(id, new_customer):
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            CUSTOMERS[index] = new_customer
            break


def get_customers_by_email(email):

    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        select
            c.id,
            c.name,
            c.address,
            c.email,
            c.password
        from Customer c
        WHERE c.email = ?
        """, ( email, ))

        customers = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            customer = Customer(row['id'], row['name'], row['address'], row['email'] , row['password'])
            customers.append(customer.__dict__)

    return json.dumps(customers)
