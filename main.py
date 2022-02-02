"""
Text Monster Game

The goal of this game is to beat the monsters and claim the prize at the end of the dungeon.
"""

# Map of the dungeon
# Feel free to adapt and design your own level. The whole map must be at least 3 floors and 15 rooms total, though.

SWORD = 0
MAGIC_STONES = 1
PRIZE = 2
EMPTY = 3
STAIRS_UP = 4
STAIRS_DOWN = 5
MONSTER = 6
BOSS_MONSTER = 7
CORPSE = 8
LEFT = -1
RIGHT = 1

the_map = [
    [EMPTY, SWORD, STAIRS_UP, MONSTER, EMPTY],
    [MAGIC_STONES, MONSTER, STAIRS_DOWN, EMPTY, STAIRS_UP],
    [PRIZE, BOSS_MONSTER, SWORD, SWORD, STAIRS_DOWN],
]

MIN_ROOM = 0
MAX_ROOM = len(the_map[1]) - 1

roomDescriptions = [
    "There is a sword here!",
    "There are mysterious glowing stones here.",
    "You have found a prize!",
    "You are in an empty room.",
    "There are stairs going up.",
    "You see stairs going down.",
    "There is an angry monster here!",
    "There is an extraordinarily large unhappy monster here.",
    "This room has a foul smelling puddle.",
]

roomContents = [
    "+5 magic sword",
    "some mysterious glowing stones",
    "The Final Prize",
]

inventory = []
floor = 0
room = 0
previous_room = 0
state = "running"

while state != "win" and state != "lose":
    print(roomDescriptions[the_map[floor][room]])
    command = input("What will you do? ")
    if command in ("help", "h", "?"):
        print(
            "You may go left (l), right (r), up (u) or down (d). You can get and fight. You may also check your bag."
        )
        
    elif command in ("get", "grab", "pick up", "g"):
        if the_map[floor][room] >= EMPTY:
            print("There is nothing to get.")
        elif len(inventory) >= 3:
            print("You can only carry three things.")
        else:
            print("You get " + roomContents[the_map[floor][room]] + ".")
            if the_map[floor][room] == PRIZE:
                state = "win"
            inventory.append(the_map[floor][room])
            the_map[floor][room] = EMPTY

    elif command in ["fight", "kill", "f"]:
        ready_for_monster = SWORD in inventory
        ready_for_boss = ready_for_monster and MAGIC_STONES in inventory
        monster_here = the_map[floor][room] == MONSTER
        boss_here = the_map[floor][room] == BOSS_MONSTER
        if not monster_here and not boss_here:
            print("Relax, there is nothing to fight here.")
        elif monster_here and not ready_for_monster:
            print("The monster kills you in a most horrible way.")
            state = "lose"
        elif boss_here and not ready_for_boss:
            print(
                "You are unprepared. The surprisingly big monster cheerfully kills you."
            )
            state = "lose"
        else:
            print(
                "You slay the evil beast and it dissolves. Unfortunately, your sword also dissolves."
            )
            inventory.remove(SWORD)
            the_map[floor][room] = CORPSE

    elif command in ["bag", "b", "inventory"]:
        if len(inventory) == 0:
            print("Your bag is empty.")
        else:
            print(inventory)

    elif command in ["up", "u"]:
        if the_map[floor][room] == STAIRS_UP:
            floor += 1
        else:
            print("There are no stairs going up.")

    elif command in ["down", "d"]:
        if the_map[floor][room] == STAIRS_DOWN:
            floor -= 1
        else:
            print("There are no stairs going down.")

    elif command in ["left", "l", "right", "r"]:
        if command in ["left", "l"]:
            direction = LEFT
            command = "left"
        else:
            direction = RIGHT
            command = "right"
        there_is_a_monster = the_map[floor][room] in [MONSTER, BOSS_MONSTER]
        going_back = room + direction == previous_room
        if there_is_a_monster and not going_back:
            print("The monster won't let you pass! You have died trying.")
            state = "lose"
        elif (direction == LEFT and room == MIN_ROOM) or (
            direction == RIGHT and room == MAX_ROOM
        ):
            print("You can't go " + command + ".")
        else:
            previous_room = room
            room += direction

    else:
        print('Command not recognized. Type "help" to see commands.')

if state == "win":
    print("You won the game! :)")
else:
    print("You lost the game. :( Maybe next time.")
