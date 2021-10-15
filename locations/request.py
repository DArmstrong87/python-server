import sqlite3
import json
from models import Location

LOCATIONS = [
    {
        "id": 1,
        "name": "Nashville South"
    },
    {
        "id": 2,
        "name": "Nashville North"
    },
    {
        "id": 3,
        "name": "Atlanta"
    }
]


def get_all_locations():
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
            a.address
        FROM location a
        """)

        # Initialize an empty list to hold all location representations
        locations = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an location instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Location class above.
            location = Location(row['id'], row['name'],
                                row['address'])

            locations.append(location.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(locations)


def get_single_location(id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address
        FROM location a
        WHERE a.id = ?
        """, (id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an location instance from the current row
        location = Location(data['id'], data['name'],
                            data['address'])

        return json.dumps(location.__dict__)


def create_location(new_location):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()
        db_cursor.execute("""
        INSERT INTO Location
            (name, address)
        VALUES (?,?)
        """,
        (new_location['name'], new_location['address'])
        )

        id = db_cursor.lastrowid
        new_location['id'] = id
    
    return json.dumps(new_location)


def delete_location(id):
    location_index = -1

    for index, location in enumerate(LOCATIONS):
        if location["id"] == id:
            location_index = index

    if location_index >= 0:
        LOCATIONS.pop(location_index)


def update_location(id, new_location):
    for index, location in enumerate(LOCATIONS):
        if location["id"] == id:
            LOCATIONS[index] = new_location
            break
