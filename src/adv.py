from room import Room
from player import Player
from item import Item
# Creat items
sword = Item("sword", "an old rusty sword")
shovel = Item("shovel", "a dirty shovel")
pickaxe = Item("pickaxe", "a steel pickaxe")
bucket = Item("bucket", "it's full of water")
coins = Item("coins", "a bag of gold coins")
spoon = Item("spoon", "a silver spoon")
torch = Item("torch", "a burning torch")
gold_cup = Item("gold cup", "a jewled cup made of gold")

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
earlier adventurers. The only exit is to the south.""", [coins, spoon, gold_cup]),
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
player_name = input(
    "\nHello! Your objective is to obtain the gold cup and exit the cave\nWhat is your name?\n")
new_player = Player(player_name, room["outside"], [])
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


def get_current_room_info():
    print("\n")
    print(new_player.current_room.name)
    print(new_player.current_room.description)
    print(f"Items: {new_player.current_room.items}")
    print("\n")


def no_room():
    print("\n")
    print("There is no room in that direction")
    print("\n")


print(new_player.current_room.name)
print(new_player.current_room.description)
print("\n")
user = input("[n] North [s] South [e] East [w] West [q] Quit\n")


while not user == 'q':
    if user == 'n':
        if new_player.current_room.n_to != 0:
            new_room = new_player.current_room.n_to
            new_player.current_room = new_room
            get_current_room_info()

        else:
            no_room()
    if user == 's':
        if new_player.current_room.s_to != 0:
            new_room = new_player.current_room.s_to
            new_player.current_room = new_room
            get_current_room_info()
        else:
            no_room()
    if user == 'e':
        if new_player.current_room.e_to != 0:
            new_room = new_player.current_room.e_to
            new_player.current_room = new_room
            get_current_room_info()
        else:
            no_room()
    if user == 'w':
        if new_player.current_room.w_to != 0:
            new_room = new_player.current_room.w_to
            new_player.current_room = new_room
            get_current_room_info()
        else:
            no_room()
    if user[:3] == 'get':
        item_to_pick_up = user[4:]

        def filter_items(x):
            if x.name == item_to_pick_up:
                new_player.inventory.append(x)
                x.on_take()
                return False
            else:
                return True
        new_room_items = filter(filter_items, new_player.current_room.items)
        new_room_items_list = []
        for y in new_room_items:
            new_room_items_list.append(y)
        if len(new_room_items_list) != len(new_player.current_room.items):
            new_player.current_room.items = new_room_items_list
            get_current_room_info()
        else:
            print("\nThat item isn't in this room\n")
    if user[:4] == 'take':
        item_to_pick_up = user[5:]

        def filter_items(x):
            if x.name == item_to_pick_up:
                new_player.inventory.append(x)
                x.on_take()
                return False
            else:
                return True
        new_room_items = filter(filter_items, new_player.current_room.items)
        new_room_items_list = []
        for y in new_room_items:
            new_room_items_list.append(y)
        if len(new_room_items_list) != len(new_player.current_room.items):
            new_player.current_room.items = new_room_items_list
            get_current_room_info()
        else:
            print("\nThat item isn't in this room\n")
    if user[:4] == 'drop':
        item_to_drop = user[5:]

        def filter_items(x):
            if x.name == item_to_drop:
                new_player.current_room.items.append(x)
                x.on_drop()
                return False
            else:
                return True
        new_inventory = filter(filter_items, new_player.inventory)
        new_inventory_list = []
        for y in new_inventory:
            new_inventory_list.append(y)
        if len(new_inventory_list) != len(new_player.inventory):
            new_player.inventory = new_inventory_list
            get_current_room_info()
        else:
            print("\nThat item isn't in your inventory\n")
    if user == 'i' or user == 'inventory':
        print(f"\n Inventory: {new_player.inventory} \n")
    if new_player.current_room.name == 'Outside Cave Entrance':
        for x in new_player.inventory:
            if x.name == 'gold cup':
                print(f"Congratulations {new_player.name}! You have won!")
                exit()

    user = input(
        "[n] North [s] South [e] East [w] West \n[i/inventory] Player Inventory [get `item name`] Pick up Item [drop `item name`] Drop Item \n[q] Quit\n")
