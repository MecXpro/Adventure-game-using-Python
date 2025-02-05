#Candidate no:291736
"""
This class is the main class of the "Adventure Adventure" application.
'Adventure Adventure' is a text-based adventure game where players explore locations,
collect items, and complete objectives.

To play this game, run this file.
"""

from room import Room
from text_ui import TextUI
from backpack import Backpack


class Game:
    def __init__(self):
        self.rooms = {}
        self.current_room = None
        self.backpack = Backpack(5)  # Player can carry 5 items max
        self.ui = TextUI()
        self.locked_rooms = {
            "treasury": "291736",  # Room name and corresponding password (candidate number)
        }

    def create_world(self):
        """Creates the game world with rooms and items."""
        # Creating rooms
        self.rooms['forest'] = Room("in the dense forest with towering trees")
        self.rooms['cabin'] = Room("in the small wooden cabin with a mysterious vibe")
        self.rooms['river'] = Room("in the flowing river with a rickety bridge")
        self.rooms['cave'] = Room("in the dark cave echoing eerie sounds")
        self.rooms['clearing'] = Room("in the sunny clearing with flowers blooming")
        self.rooms['garden'] = Room("in the lush garden with vibrant flowers")
        self.rooms['tower'] = Room("in the tall stone tower overlooking the land")
        self.rooms['treasury'] = Room("in the locked treasury containing valuable items")
        self.rooms['library'] = Room("in the quiet library filled with ancient books")
        self.rooms['cellar'] = Room("in the dimly lit cellar with old barrels")

        # Set exits for rooms
        self.rooms['forest'].set_exit('east', self.rooms['cabin'])
        self.rooms['forest'].set_exit('south', self.rooms['river'])
        self.rooms['cabin'].set_exit('west', self.rooms['forest'])
        self.rooms['cabin'].set_exit('down', self.rooms['cave'])
        self.rooms['river'].set_exit('north', self.rooms['forest'])
        self.rooms['river'].set_exit('east', self.rooms['clearing'])
        self.rooms['cave'].set_exit('up', self.rooms['cabin'])
        self.rooms['clearing'].set_exit('west', self.rooms['river'])
        self.rooms['clearing'].set_exit('north', self.rooms['garden'])
        self.rooms['garden'].set_exit('north', self.rooms['tower'])
        self.rooms['tower'].set_exit('south', self.rooms['garden'])
        self.rooms['tower'].set_exit('east', self.rooms['treasury'])
        self.rooms['treasury'].set_exit('west', self.rooms['tower'])
        self.rooms['library'].set_exit('west', self.rooms['cave'])
        self.rooms['cellar'].set_exit('north', self.rooms['library'])

        # Add items to rooms
        self.rooms['cabin'].add_item("key")
        self.rooms['clearing'].add_item("flower")
        self.rooms['cave'].add_item("torch")
        self.rooms['treasury'].add_item("Full Marks in Assignment")

        # Set the starting room
        self.current_room = self.rooms['forest']

    def play(self):
        """Main gameplay loop."""
        self.create_world()
        self.ui.show_welcome()

        while True:
            self.ui.show_location(self.current_room)
            command = self.ui.get_command()

            if command[0] == 'go':
                self.go_room(command[1])
            elif command[0] == 'take':
                self.take_item(command[1])
            elif command[0] == 'inventory':
                self.ui.show_inventory(self.backpack.contents)
            elif command[0] == 'unlock':
                self.unlock_room(command[1])
            elif command[0] == 'quit':
                print("Thanks for playing!")
                break
            else:
                print("I don't understand that command.")

    def go_room(self, direction):
        """Moves the player in the specified direction."""
        next_room = self.current_room.get_exit(direction)
        if next_room:
            if next_room in self.locked_rooms:
                print("This room is locked. Use 'unlock <room_name>' to access it.")
            else:
                self.current_room = next_room
        else:
            print("You can't go that way.")

    def take_item(self, item):
        """Player attempts to pick up an item."""
        if self.current_room.has_item(item):
            try:
                self.backpack.add_item(item)
                self.current_room.remove_item(item)
                print(f"You have picked up the {item}.")
            except Exception as e:
                print(e)
        else:
            print("That item is not here.")

    def unlock_room(self, room_name):
        """Unlocks a locked room if the correct password is provided."""
        if room_name in self.locked_rooms:
            password = input("Enter the password: ")
            if password == self.locked_rooms[room_name]:
                print(f"The {room_name} is now unlocked!")
                del self.locked_rooms[room_name]
            else:
                print("Incorrect password. Hint: It's your candidate number.")
        else:
            print("This room is not locked or doesn't exist.")


if __name__ == "__main__":
    game = Game()
    game.play()
