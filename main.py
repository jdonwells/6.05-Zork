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


def help():
    print(
        "You may go left (l), right (r), up or down. You can get and fight. You may also check your bag."
    )


def left():
    move("left")


def right():
    move("right")


def move(direction):
    global previous_room, room, state
    room_change = {"left": -1, "right": 1}
    there_is_a_monster = this_room() in monsters
    going_back = room + room_change[direction] == previous_room
    last_room = (
        first_room_on_this_floor(floor)
        if direction == "left"
        else last_room_on_this_floor(floor)
    )
    if there_is_a_monster and not going_back:
        print("The monster won't let you pass! You have died trying.")
        state = "lose"
        return
    if room == last_room:
        print(f"You can't go {direction}.")
        return
    previous_room = room
    room += room_change[direction]


def up():
    global floor
    if this_room() == "stairs up":
        floor += 1
    else:
        print("There are no stairs going up.")


def down():
    global floor
    if this_room() == "stairs down":
        floor -= 1
    else:
        print("There are no stairs going down.")


def get():
    global state
    if this_room() not in roomContents:
        print("There is nothing to get.")
        return
    if len(inventory) >= 3:
        print("You can only carry three things.")
        return
    print("You get {}".format(roomContents[this_room()]))
    if this_room() == "prize":
        state = "win"
    inventory.append(this_room())
    empty_this_room(floor, room)


def fight():
    global state
    ready_for_monster = "sword" in inventory
    ready_for_boss = ready_for_monster and "magic stones" in inventory
    monster_here = this_room() == "monster"
    boss_here = this_room() == "boss monster"
    if not monster_here and not boss_here:
        print("Relax, there is nothing to fight here.")
        return
    if monster_here and not ready_for_monster:
        print("The monster kills you in a most horrible way.")
        state = "lose"
        return
    if boss_here and not ready_for_boss:
        print("You are unprepared. The surprisingly big monster cheerfully kills you.")
        state = "lose"
        return
    print(
        "You slay the evil beast and it dissolves. Unfortunately, your sword also dissolves."
    )
    inventory.remove("sword")
    monster_died_here(floor, room)


def bag():
    if len(inventory) == 0:
        print("Your bag is empty.")
        return
    print(", ".join([roomContents[item] for item in inventory]))


def this_room():
    return map[floor][room]


def first_room_on_this_floor(__):
    return 0


def last_room_on_this_floor(floor):
    global map
    return len(map[floor]) - 1


def empty_this_room(floor, room):
    global map
    map[floor][room] = "empty"


def description(floor, room):
    return roomDescriptions[map[floor][room]]


def monster_died_here(floor, room):
    global map
    map[floor][room] = "corpse"


commands = {
    "help": help,
    "left": left,
    "l": left,
    "right": right,
    "r": right,
    "up": up,
    "u": up,
    "down": down,
    "d": down,
    "get": get,
    "fight": fight,
    "bag": bag,
}


def playGame():
    # create an Adventurer to represent me. Initialize inventory to empty,
    # position to lower left room, state to game on

    global inventory, floor, room, previous_room, state

    inventory = []
    floor = 0
    room = 0
    previous_room = 0
    state = "running"

    while state != "win" and state != "lose":
        print(description(floor, room))
        command = input("What will you do? ")
        if command in commands:
            commands[command]()
        else:
            print('Command not recognized. Type "help" to see commands.')

    if state == "win":
        print("You won the game! :)")
    else:
        print("You lost the game. :( Maybe next time.")


playGame()
