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
    "corpse": "This room has a foul smelling puddle.",
    "magic stones": "There are mysterious glowing stones here.",
    "prize": "You have found a prize!",
}

monsters = ("monster", "boss monster")

roomContents = {
    "sword": "+5 magic sword",
    "magic stones": "some mysterious glowing stones",
    "prize": "The Final Prize",
}


class Adventurer:
    """
    My Adventurer class that holds game state and runs commands
    """

    def __init__(self):
        self.inventory = []
        self.floor = 0
        self.room = 0
        self.previousRoom = 0
        self.state = "running"

    def help(__):
        print(
            "You may go left (l), right (r), up or down. You can get and fight. You may also check your bag."
        )

    def left(self):
        self.move("left")

    def l(self):
        self.move("left")

    def right(self):
        self.move("right")

    def r(self):
        self.move("right")

    def move(self, direction):
        room_change = {"left": -1, "right": 1}
        there_is_a_monster = self.this_room() in monsters
        going_back = self.room + room_change[direction] == self.previousRoom
        last_room = (
            first_room_on_this_floor(self.floor)
            if direction == "left"
            else last_room_on_this_floor(self.floor)
        )
        if there_is_a_monster and not going_back:
            print("The monster won't let you pass! You have died trying.")
            self.state = "lose"
            return
        if self.room == last_room:
            print(f"You can't go {direction}.")
            return
        self.previousRoom = self.room
        self.room += room_change[direction]

    def up(self):
        if self.this_room() == "stairs up":
            self.floor += 1
        else:
            print("There are no stairs going up.")

    def down(self):
        if self.this_room() == "stairs down":
            self.floor -= 1
        else:
            print("There are no stairs going down.")

    def get(self):
        if self.this_room() not in roomContents:
            print("There is nothing to get.")
            return
        if len(self.inventory) >= 3:
            print("You can only carry three things.")
            return
        print("You get {}".format(roomContents[self.this_room()]))
        if self.this_room() == "prize":
            self.state = "win"
        self.inventory.append(self.this_room())
        empty_this_room(self.floor, self.room)

    def fight(self):
        ready_for_monster = "sword" in self.inventory
        ready_for_boss = ready_for_monster and "magic stones" in self.inventory
        monster_here = self.this_room() == "monster"
        boss_here = self.this_room() == "boss monster"
        if not monster_here and not boss_here:
            print("Relax, there is nothing to fight here.")
            return
        if monster_here and not ready_for_monster:
            print("The monster kills you in a most horrible way.")
            self.state = "lose"
            return
        if boss_here and not ready_for_boss:
            print(
                "You are unprepared. The surprisingly big monster cheerfully kills you."
            )
            self.state = "lose"
            return
        print(
            "You slay the evil beast and it dissolves. Unfortunately, your sword also dissolves."
        )
        self.inventory.remove("sword")
        monster_died_here(self.floor, self.room)

    def bag(self):
        if len(self.inventory) == 0:
            print("Your bag is empty.")
            return
        print(", ".join([roomContents[item] for item in self.inventory]))

    def this_room(self):
        return map[self.floor][self.room]


def first_room_on_this_floor(__):
    return 0


def last_room_on_this_floor(floor):
    global map
    return len(map[floor]) - 1


def empty_this_room(floor, room):
    global map
    map[floor][room] = "empty"


def description(floor, room):
    global map
    return roomDescriptions[map[floor][room]]


def monster_died_here(floor, room):
    global map
    map[floor][room] = "corpse"


def playGame():
    # create an Adventurer to represent me. Initialize inventory to empty,
    # position to lower left room, state to game on
    me = Adventurer()

    while me.state != "win" and me.state != "lose":
        print(description(me.floor, me.room))
        try:
            getattr(me, input("What will you do? "))()
        except:
            print('Command not recognized. Type "help" to see commands.')

    if me.state == "win":
        print("You won the game! :)")
    else:
        print("You lost the game. :( Maybe next time.")


playGame()
