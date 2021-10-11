ANIMALS = [
    {
      "id": 1,
      "name": "Doodles",
      "breed": "German Shepherd",
      "locationId": 1
    },
    {
      "id": 3,
      "name": "Angus",
      "breed": "Dalmatian 👾",
      "locationId": 1
    },
    {
      "id": 4,
      "name": "Henley",
      "breed": "Carolina Retriever 🚒",
      "locationId": 1
    },
    {
      "id": 5,
      "name": "Derkins",
      "breed": "Shih tzu 👿",
      "locationId": 2
    },
    {
      "id": 6,
      "name": "Checkers",
      "breed": "Bulldog",
      "locationId": 1
    },
    {
      "name": "Sawyer",
      "breed": "Lollie",
      "id": 7,
      "locationId": 2
    },
    {
      "name": "Gypsy",
      "breed": "Miniature Schnauzer",
      "id": 8,
      "locationId": 1
    },
    {
      "name": "Zipper",
      "breed": "Terrier",
      "locationId": 2,
      "id": 9
    },
    {
      "name": "Blue",
      "breed": "Hound dog",
      "locationId": 2,
      "id": 10
    },
    {
      "name": "JOE",
      "breed": "Husky",
      "locationId": 2,
      "id": 11
    }
]


def get_all_animals():
    '''Get all animals'''
    return ANIMALS
# Function with a single parameter


def get_single_animal(id):
    # Variable to hold the found animal, if it exists
    requested_animal = None

    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for animal in ANIMALS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if animal["id"] == id:
            requested_animal = animal

    return requested_animal
