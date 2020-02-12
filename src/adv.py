from room import Room
from player import Player
from item import Item
# Creat items
sword = Item("sword", "an old rusty sword")
shovel = Item("shovel", "a dirty shovel")
pickaxe = Item("pickaxe", "a steel pickaxe")
bucket = Item("bucket", "it's full of water")
gold = Item("coins", "a bag of gold coins")
silver = Item("spoon", "a silver spoon")
torch = Item("torch", "a burning torch")

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", []),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [sword, bucket]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [pickaxe, shovel, torch]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", []),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [gold, silver]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
new_player = Player("Bill", room["outside"], [])
# print(new_player.current_room.name)
# print(new_player.current_room.description)
# print(room['outside'].n_to.name)

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
user = input("[n] North [s] South [e] East [w] West [q] Quit\n")
print(new_player.current_room.name)
print(new_player.current_room.description)

while not user == 'q':
    if user == 'n':
        if new_player.current_room.n_to != 0:
            new_room = new_player.current_room.n_to
            new_player.current_room = new_room
            print(new_player.current_room.name)
            print(new_player.current_room.description)
            print(new_player.current_room.items)
        else:
            print("There is no room in that direction")
    if user == 's':
        if new_player.current_room.s_to != 0:
            new_room = new_player.current_room.s_to
            new_player.current_room = new_room
            print(new_player.current_room.name)
            print(new_player.current_room.description)
            print(new_player.current_room.items)
        else:
            print("There is no room in that direction")
    if user == 'e':
        if new_player.current_room.e_to != 0:
            new_room = new_player.current_room.e_to
            new_player.current_room = new_room
            print(new_player.current_room.name)
            print(new_player.current_room.description)
            print(new_player.current_room.items)
        else:
            print("There is no room in that direction")
    if user == 'w':
        if new_player.current_room.w_to != 0:
            new_room = new_player.current_room.w_to
            new_player.current_room = new_room
            print(new_player.current_room.name)
            print(new_player.current_room.description)
            print(new_player.current_room.items)
        else:
            print("There is no room in that direction")
    if user[:3] == 'get':
        print('Get is working')

    user = input(
        "[n] North [s] South [e] East [w] West \n[get `item name`] Pick up Item [drop `item name`] Drop Item \n[q] Quit\n")
