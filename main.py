from interface.root import *
from database.src.functions.insertion import *
from datetime import *
from database.src.utils.constants import *


def main():
    """Creates the user interface and every functionally that comes with it."""
    root = MainApplication('PAWS - Pet Grooming Store Software')
    root.run()


if __name__ == "__main__":
    main()
