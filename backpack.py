"""
Backpack module for carrying items.
"""

class Backpack:
    """A class to allow players to pick up and store items."""

    def __init__(self, capacity):
        self.contents = []  # List of items in the backpack
        self.capacity = capacity

    def add_item(self, item):
        """Adds an item to the backpack."""
        if len(self.contents) < self.capacity:
            self.contents.append(item)
        else:
            raise Exception("Your backpack is full!")

    def remove_item(self, item):
        """Removes an item from the backpack."""
        if item in self.contents:
            self.contents.remove(item)
        else:
            print(f"{item} is not in your backpack.")
