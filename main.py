from interface.root import *
from database.src.root import *


def main():
    """Creates our application by initializing the database and the user interface."""
    initDatabase()
    root = MainApplication('PAWS - Pet Grooming Store Software')
    root.run()


if __name__ == "__main__":
    main()
