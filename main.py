"""
Text Adventure Game

The goal of this game is to beat the monsters and claim the prize at the end of 
the dungeon.
"""

"""
The map and descriptions of various rooms and items. 5 character abbreviations so you
can see what the map is easily. None is used to indicate a solid wall. I have put None
around the entire map so I don't have to code exceptions for off the map indexing.
"""

dungeon_map = [
    [None,  None,    None,    None,    None,    None,    None,    None,    None,   None],
    [None, "start", "sword", "empty", "tapes", "plant", "sword", "orc",   "empty", None],
    [None,  None,    None,   "tarot",  None,    None,   "maze",   None,    None,   None],
    [None, "kitch", "sword", "orc",    None,   "maze",  "maze",  "maze",  "maze",  None],
    [None, "leavs",  None,    None,    None,   "maze",   None,   "maze",  "maze",  None],
    [None, "tapes",  None,   "plant",  None,   "spidr", "maze",   None,   "maze",  None],
    [None, "libry", "tunlN", "store",  None,    None,    None,   "maze",  "maze",  None],
    [None,  None,   "tunnl",  None,    None,   "halbd", "mazOW", "maze",   None,   None],
    [None, "sword", "tunlS", "puddl",  None,    None,   "hole",   None,    None,   None],
    [None,  None,    None,   "bigNW", "bigNE", "plant", "kitch", "troll", "tapes", None],
    [None, "stnes", "thron", "bigSW", "bigSE", "sword",  None,    None,   "empty", None],
    [None,  None,    None,   "troll",  None,    None,    None,   "prize", "troll", None],
    [None,  None,    None,    None,    None,    None,    None,    None,    None,   None],
]

room_descriptions = {
    # things you can pick up
    "sword": "This is an unremarkable room. There is a rusty old sword here!",
    "halbd": "So many rusted and broken weapons. There is one that stands out. "
             "A halberd decorated with gold and silver that glows with some "
             "kind of magic.",
    "stnes": "There are mysterious glowing stones here.",
    "prize": "You have found a prize!",
    # an empty room for after you pick up the thing
    "empty": "You are in an empty room.",
    # some different rooms that just have discriptions and can be used and reused
    "start": "You are stuck at the bottom of a dry well. There is a moldy" 
             " door to the East that you forced open.",
    "thron": "You are in a throne room complete with a large gaudy chair. "
             "You imagine it was resplendent in gold and red before it all "
             "faded to brown and grey.",
    "tapes": "You have found a room with large faded tapestries on the walls. "
             "Moths have chewed holes in some of them.",
    "puddl": "A foul smelling puddle makes you feel a bit ill.",
    "kitch": "This room has a very large cauldron over a burnt out fire pit. "
             "From the bones piled neatly in the corner you surmise adventurers"
             " are cooked and eaten here.",
    "tarot": "A goblin with gaudy makeup is sitting at a table with tarot cards"
             " laid out in front of her. She looks up as you enter. She flips a "
             'card and gives you your fortune: "Death".',
    "store": "This was once a room full of crates and barrels to store "
             "important things. Everything has been broken open and emptied. "
             "What a mess.",
    "libry": "This library is in poor condition. The books crumble to dust when "
             "you touch them. Ironically, as you pick up a novel by Margaret "
             "Mitchell it turns to dust and blows away in a cool draft of air.",
    # a tight tunnel that takes up 3 spaces
    "tunlN": "A small tunnel goes South. You might be able to squeeze through.",
    "tunnl": "You are in a tunnel just big enough to squeeze through.",
    "tunlS": "A small tunnel goes North. You might be able to squeeze through.",
    # The maze uses the same discription over and over to confuse the player.
    # There is a way to get out with the halberd and get to the prize.
    "maze" : "You are in a maze of twisty little passages, all alike.",
    "mazOW": "You are in a maze of twisty little passages. There is a hole in"
             " the wall to the South with a ladder to reach it. If you go "
             "through it you may not get back.",
    "hole" : "There is a hole near the ceiling to the North, if you stack a few "
             "dead bodies up you might be able to reach it.",
    # a big cave that takes up 4 locations on the map. It discribes an orc troll war.
    "bigNW": "This is an enormous cave. It looks like a war between orcs and "
             "trolls has been going on here for a while. You are in the North"
             " West corner.",
    "bigNE": "This is an enormous cave. The war between orcs and trolls has "
             "been brutal. You are in the North East corner.",
    "bigSW": "This is an enormous cave. Dead orcs and trolls are every where. "
             "You are in the South West corner.",
    "bigSE": "This is an enormous cave. It looks like a war between orcs and "
             "trolls started here. You are in the South East corner.",
    # monsters that want to kill you.
    "orc"  : "There is an angry orc here! He is going to kill you without "
             "any further discussion.",
    "troll": "An extraordinarily large, unhappy troll is sitting here. He "
             "isn't going to let you pass without extracting a cost.",
    "plant": "There is a huge carnivorous plant growing out of a large crack "
             "in the floor. It is snapping at you. You could try sneaking around "
             "it, but it will probably eat you.",
    "spidr": "A very large spider sits motionless in an even larger web.",
    # dead versions of all the monsters that didn't kill you.
    "corpse": "You find a dead orc just laying there.",
    "troll corpse": "A dead troll is sprawled out across the room. "
                "You will need to climb over him.",
    "leavs": "This room is littered with very large dried up leaves.",
    "gooey web": "There is a large spider web with some kind of goo all over it.",
}

item_descriptions = {
    "sword": "a rusty sword",
    "stnes": "some mysterious glowing stones",
    "halbd": "a glowing ceremonial halberd",
    "prize": "The Final Prize",
}

death_by_monster = {
    "orc"  : "The orc kills you in a most horrible way.",
    "troll": "You are unprepared. The surprisingly big troll cheerfully kills you.",
    "plant": "You are grabbed by the large plant and slowly digested over the next "
             "couple of days.",
    "spidr": "The spider grabs you with amazing speed and agility. You will be "
             "eaten in a few days. Enjoy hanging out with the spider.",
}

kill_the_monster = {
    "orc"  : "You manage to kill the orc.",
    "troll": "The surprisingly big troll also dies surprisingly easy.",
    "plant": "You hack the plant into pieces. The large leaves are "
             "already turning brown.",
    "spidr": "You stab the overgrown spider and it oozes in a disgusting way.",
}

monster_to_corpse = {
    "orc"  : "corpse",
    "troll": "troll corpse",
    "plant": "leavs",
    "spidr": "gooey web",
}

"""
Room locations and code to manipulate them.

A room location is a list of two integers. The first or 0 element
is the north-south index. The second or 1 element is the east-west
index.
"""

moves = {
        "east" : [0, 1], 
        "west" : [0, -1], 
        "north": [-1, 0], 
        "south": [1, 0]
    }


def start_location():
    return [1, 1]


def change_room(direction):
    return [room[0] + moves[direction][0], room[1] + moves[direction][1]]


def room_type(here):
    return dungeon_map[here[0]][here[1]]


def this_room():
    return room_type(room)


def set_room_type(type):
    global dungeon_map
    dungeon_map[room[0]][room[1]] = type

    
def room_exists(a_room):
    return room_type(a_room) != None


def empty_this_room():
    set_room_type("empty")


def description():
    return room_descriptions[this_room()]


def monster_died_here():
    set_room_type(monster_to_corpse[this_room()])


"""
Functions to run the various commands you can enter.
"""


def help():
    print(
        "You may go West (w), East (e), up (u) or down (d) if there is an exit.",
        "You can get (g) and fight (f). You may also check your bag (b).",
        "To repeat the room description use look (l). To repeat this type help.",
        "\n"
    )


def west():
    move("west")


def east():
    move("east")


def north():
    move("north")


def south():
    move("south")


def look():
    print(description())
    print(exits())


def get():
    global state
    if this_room() not in item_descriptions:
        print("There is nothing to get.")
    else:
        print("You get " + item_descriptions[this_room()] + ".")
        if this_room() == "prize":
            state = "win"
        bag.append(this_room())
        empty_this_room()


def fight():
    global state
    if not there_is_a_monster_here():
        print("Relax, there is nothing to fight here.")
    elif (
        (there_is_a_monster_here() and not ready_for_monster()) or 
        (there_is_a_troll_here() and not ready_for_troll())
    ):  # even Python is sad about it
        print(death_by_monster[this_room()])
        state = "lose"
    else:
        print(kill_the_monster[this_room()])
        if not "halbd" in bag:
            print("Your rusty old sword breaks. You won't be using it again.")
            bag.remove("sword")
        monster_died_here()


def bag_contents():
    if len(bag) == 0:
        print("Your bag is empty.")
    else:
        for item in bag:
            print(item_descriptions[item])


def unknown():
    print('Command not recognized. Type "help" to see commands.')


"""
Functions that help other functions in some way.
"""


def move(direction):
    global previous_room, room, state
    new_room = change_room(direction)
    going_back = new_room == previous_room
    if not room_exists(new_room):
        print("You can't go that way.")
    elif there_is_a_monster_here() and not going_back:
        print("The monster won't let you pass!", death_by_monster[this_room()])
        state = "lose"
    else:
        previous_room = room
        room = new_room
        look()


def exits():
    good_exits = [
        direction for direction in ["east", "west", "north", "south"] 
        if room_exists(change_room(direction))
    ]
    description = "You can go "
    if len(good_exits) == 1:
        description = description + good_exits[0]
    else:
        for direction in good_exits[0:-1]:
            description = description + direction + ", "
        description = description + "or " + good_exits[-1]
    return description + "."


def there_is_a_monster_here():
    return this_room() in death_by_monster


def there_is_a_troll_here():
    return this_room() == "troll"


def ready_for_monster():
    return "sword" in bag or "halbd" in bag


def ready_for_troll():
    return ("sword" in bag and "stnes" in bag) or "halbd" in bag


def initialize():
    global bag, room, previous_room, state
    bag = []
    room = start_location()
    previous_room = start_location()
    state = "playing"


def print_winner():
    # Way back before digital images there was ASCII art.
    line4 = (" "*3+"/ / //"+" "*3+"// //"+" "*3+"//"+" "*4+"||/ / |  / " +
             "// //"+" "*3+"//")
    line7 = " "*21+"/| "+"_"*16
    line3 = ("  \\\\/ / //"+" "*3+")) //"+" "*3+"//"+" "*3+"|| / /||/ " +
             "/ // //"+" "*3+"))  //")
    line1 = "\\\\"+" "*4+"/ /"+" "*17+"||"+" "*3+"/ |  / /"+" "*13+"//"
    line5 = (" "*2+"/ / (("+"_"*3+"// (("+"_"*3+"(("+" "*5+"|  /  | / /" +
             "/ //"+" "*3+"//  //")
    line8 = " "*15+"O|"+"="*3+"|* >"+"_"*16+">"
    line2 = " \\\\  / /  ___"+" "*13+"||  /  | / "+"/ ()  ___"+" "*5+"//"
    line9 = " "*21+"\|"
    if state == "win":
        print(
            "", "", line1, line2, line3, line4, line5, 
            "", line7, line8, line9,
            "", "", "You have won the game.", 
            sep="\n"
        )
    else:
        print("You lost the game. Maybe next time.")


"""
A dictionary that translates a command into a function that needs to be called.
To add new commands just add the command's name as a key and a function name 
as the value.
"""

commands = {
    "help": help,
    "west": west, "w": west,
    "east": east, "e": east,
    "south": south, "s": south,
    "north": north, "n": north,
    "get": get, "g": get,
    "fight": fight, "f": fight,
    "bag": bag_contents, "b": bag_contents,
    "look": look, "l": look,
}


def welcome():
    print("Welcome to my Text Adventure Game. Kill the monsters, survive, and find the Final Prize to win!\n")


def play_game():
    """
    Start up my text adventure game. Uses the console for everything.
    """
    initialize()
    welcome()
    help()
    look()
    while state == "playing":
        # Process commands with a dictionary. If the command is in the dictionary
        # call the value as a function. If not call the default function unknown().
        commands.get(input("What will you do? "), unknown)()
    print_winner()


play_game()