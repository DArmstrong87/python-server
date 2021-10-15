import sqlite3
import json
from models import Animal
from models import Location
from models import Customer

ANIMALS = [
    {
        "id": 1,
        "name": "Doodles",
        "breed": "German Shepherd",
        "locationId": 1,
        "status": "Admitted"
    },
    {
        "id": 2,
        "name": "Josephine",
        "breed": "Rottweiler",
        "locationId": 1,
        "status": "Admitted"
    },
    {
        "id": 3,
        "name": "Angus",
        "breed": "Dalmatian 👾",
        "locationId": 1,
        "status": "Admitted"
    },
    {
        "id": 4,
        "name": "Henley",
        "breed": "Carolina Retriever 🚒",
        "locationId": 1,
        "status": "Admitted"
    },
    {
        "id": 5,
        "name": "Derkins",
        "breed": "Shihtzu 👿",
        "locationId": 2,
        "status": "Admitted"
    },
    {
        "id": 6,
        "name": "Checkers",
        "breed": "Bulldog",
        "locationId": 1,
        "status": "Admitted"
    },
    {
        "name": "Sawyer",
        "breed": "Lollie",
        "id": 7,
        "locationId": 2,
        "status": "Admitted"
    },
    {
        "name": "Gypsy",
        "breed": "Miniature Schnauzer",
        "id": 8,
        "locationId": 1,
        "status": "Admitted"
    },
    {
        "name": "Zipper",
        "breed": "Terrier",
        "locationId": 2,
        "id": 9,
        "status": "Admitted"
    },
    {
        "name": "Blue",
        "breed": "Hound dog",
        "locationId": 2,
        "id": 10,
        "status": "Admitted"
    },
    {
        "name": "JOE",
        "breed": "Husky",
        "locationId": 2,
        "id": 11,
        "status": "Admitted"
    }
]


def get_all_animals():
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
            a.breed,
            a.status,
            a.location_id,
            a.customer_id,
            l.id loc_id,
            l.name location_name,
            l.address location_address,
            c.id cust_id,
            c.name customer_name,
            c.address customer_address
        FROM Animal a
        JOIN Location l
            ON l.id = a.location_id
        JOIN Customer c
            ON c.id = a.customer_id
        """)

        # Initialize an empty list to hold all animal representations
        animals = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an animal instance from the current row
            animal = Animal(row['id'], row['name'], row['breed'],
                            row['status'], row['location_id'], row['customer_id'])

            # Create a Location instance from the current row
            location = Location(
                row['loc_id'], row['location_name'], row['location_address'])

            customer = Customer(
               row['cust_id'], row['customer_name'], row['customer_address']
            )

            # Add the dictionary representation of the location to the animal
            animal.location = location.__dict__
            animal.customer = customer.__dict__

            # Add the dictionary representation of the animal to the list
            animals.append(animal.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(animals)


def get_single_animal(id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.location_id,
            a.customer_id
        FROM animal a
        WHERE a.id = ?
        """, (id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        animal = Animal(data['id'], data['name'], data['breed'],
                        data['status'], data['location_id'],
                        data['customer_id'])

        return json.dumps(animal.__dict__)


def create_animal(new_animal):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Animal
            ( name, breed, status, location_id, customer_id )
        VALUES
            ( ?, ?, ?, ?, ?);
        """, (new_animal['name'], new_animal['breed'],
              new_animal['status'], new_animal['location_id'],
              new_animal['customer_id'], ))

        # The `lastrowid` property on the cursor will return
        # the primary key of the last thing that got added to
        # the database.
        id = db_cursor.lastrowid

        # Add the `id` property to the animal dictionary that
        # was sent by the client so that the client sees the
        # primary key in the response.
        new_animal['id'] = id


    return json.dumps(new_animal)



def delete_animal(id):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM animal
        WHERE id = ?
        """, (id, ))


def update_animal(id, new_animal):
    # Iterate the ANIMALS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, animal in enumerate(ANIMALS):
        if animal["id"] == id:
            # Found the animal. Update the value.
            ANIMALS[index] = new_animal
            break


def get_animals_by_location(location_id):

    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.location_id,
            a.customer_id
        FROM animal a
        WHERE a.location_id = ?
        """, (location_id, ))

        animals = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            animal = Animal(row['id'], row['name'], row['breed'],
                            row['status'], row['location_id'], row['customer_id'])
            animals.append(animal.__dict__)

    return json.dumps(animals)


def get_animals_by_status(status):

    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.location_id,
            a.customer_id
        FROM animal a
        WHERE a.status = ?
        """, (status, ))

        animals = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            animal = Animal(row['id'], row['name'], row['breed'],
                            row['status'], row['location_id'], row['customer_id'])
            animals.append(animal.__dict__)

    return json.dumps(animals)
