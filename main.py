"""
Text Monster Game

The goal of this game is to beat the monsters and claim the prize at the end of the dungeon.
"""

# Map of the dungeon
# Feel free to adapt and design your own level. The whole map must be at least 3 floors and 15 rooms total, though.
map = [
    ["empty", "sword", "stairs up", "monster", "empty"],
    ["magic stones", "monster", "stairs down", "empty", "stairs up"],
    ["prize", "boss monster", "sword", "sword", "stairs down"],
]

roomDescriptions = {
    "empty": "You are in an empty room.",
    "sword": "There is a sword here!",
    "stairs up": "There are stairs going up.",
    "stairs down": "You see stairs going down.",
    "monster": "There is an angry monster here!",
    "boss monster": "There is an extraordinarily large unhappy monster here.",
    "magic stones": "There are mysterious glowing stones here.",
    "prize": "You have found a prize!",
}

roomContents = {
    "sword": "sword",
    "magic stones": "mysterious glowing stones",
    "prize": "prize",
}


class Adventurer:
    """ 
    My Adventurer class that holds game state and runs commands
    """
    def __init__(self):
        self.inventory = []
        self.floor = 0
        self.room = 0
        self.state = "ongoing"

    def help(__):
        print(
            "You may go left, right, up or down. You may also get and fight. You may check your bag with inventory."
        )

    def left(self):
        if self.room > 0:
            self.room -= 1
        else:
            print("You can't go left.")

    def right(self):
        if self.room < len(map[self.floor]) - 1:
            self.room += 1
        else:
            print("You can't go right.")

    def up(self):
        if map(self.floor, self.room) == "stairs up":
            self.floor += 1
        else:
            print("There are no stairs here.")

    def down(self):
        if map(self.floor, self.room) == "stairs down":
            self.floor -= 1
        else:
            print("There are no stairs here.")

    def get(self):
        return

    def fight(self):
        return

    def inventory(self):
        return


def description(floor, room):
    return roomDescriptions[map[floor][room]]


def playGame():
    # create an Adventurer to represent me. Initialize inventory to empty,
    # position to lower left room, state to game on
    me = Adventurer()

    while me.state == "ongoing":
        print(description(me.floor, me.room))
        try:
            getattr(me, input("What will you do? "))()
        except:
            print('Command not recognized. Type "help" to see commands.')

    if me.state == "won":
        print("You won the game! :)")
    else:
        print("You lost the game. :( Maybe next time.")


playGame()
