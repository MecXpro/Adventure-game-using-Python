"""
A simple text-based User Interface (UI) for the Adventure Game.
"""

class TextUI:
    """A simple text-based User Interface for the game."""

    def show_welcome(self):
        """Displays the welcome message."""
        print("Welcome to Adventure Adventure!")
        print("Explore the world, collect items, and enjoy!")
        self.show_guide()

    def show_guide(self):
        """Displays the guide for controls and locations."""
        print("\n--- Game Guide ---")
        print("Controls:")
        print("  - 'go <direction>': Move to a connected room (e.g., 'go east').")
        print("  - 'take <item>': Pick up an item in the current room (e.g., 'take key').")
        print("  - 'unlock <room_name>': Unlock a locked room by entering the password.")
        print("  - 'inventory': View the items in your backpack.")
        print("  - 'quit': Exit the game.")
        print("\nLocations:")
        print("  - Forest: Starting point, leads to Cabin (east) and River (south).")
        print("  - Cabin: Contains a key, leads to Forest (west) and Cave (down).")
        print("  - River: Leads to Forest (north) and Clearing (east).")
        print("  - Cave: Contains a torch, leads back to Cabin (up).")
        print("  - Clearing: Contains a flower, leads to River (west) and Garden (north).")
        print("  - Garden: Leads to Tower (north).")
        print("  - Tower: Leads to Treasury (east).")
        print("  - Treasury: Locked room containing a special item (unlock with password).")
        print("-------------------\n")

    def show_location(self, room):
        """Displays the player's current location."""
        print(room.get_long_description())

    def show_inventory(self, contents):
        """Displays the items in the player's backpack."""
        if contents:
            print("You have: " + ", ".join(contents))
        else:
            print("Your backpack is empty.")

    def get_command(self):
        """Fetches a command from the console."""
        print("> ", end="")
        input_line = input().strip()
        words = input_line.split()
        word1 = words[0] if len(words) > 0 else None
        word2 = words[1] if len(words) > 1 else None
        return word1, word2
