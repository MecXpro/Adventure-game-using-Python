"""
Room module for managing locations in the adventure game.
"""

class Room:
    """A room in the adventure game."""

    def __init__(self, description):
        self.description = description
        self.exits = {}  # Dictionary to hold exits
        self.items = []  # List to hold items in the room

    def set_exit(self, direction, neighbour):
        """Adds an exit to this room."""
        self.exits[direction] = neighbour

    def add_item(self, item):
        """Adds an item to this room."""
        self.items.append(item)

    def remove_item(self, item):
        """Removes an item from this room."""
        if item in self.items:
            self.items.remove(item)

    def has_item(self, item):
        """Checks if an item is in the room."""
        return item in self.items

    def get_exit(self, direction):
        """Gets the room in the given direction."""
        return self.exits.get(direction, None)

    def get_long_description(self):
        """Returns a description of the room."""
        description = f"You are {self.description}.\n"
        if self.items:
            description += f"You see: {', '.join(self.items)}.\n"
        return description
