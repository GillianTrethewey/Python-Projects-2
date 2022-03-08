def main():

    get_name()
    start_adventure()  
    print("\nThe end\n")

def get_name():

    name = input("What's your name?  ")
    name = name.strip().upper()
    print("Nice to meet you,",name,"!")

    return name

def start_adventure():
    print(
           "The object of the game is to gather three candy items.\n"
        "Once you have all the candy, go to the hotel front door to escape."
        )
    locations['lobby'].visit(count)

HOTEL_FRONT_DOOR = 'hotel front door'
inventory = []
door = ["locked"]
count = 0
class Location:
    def __init__(self, text, locations={}, items=[], name=''):
        self.text = text
        self.locations = locations
        self.items = items
        self.name = name


    def describe(self):
        print(self.text)
        for item in self.items:
            print('There is a', item, 'here.')
        for direction in self.locations:
            print(direction, self.locations[direction])

    def chambermaid(self):
        if count % 2 == 0 and (self.name == 'storage room' or self.name == 'the blue hallway'):
            print("The chambermaid is here, dancing to remember.")
        elif count %2 != 0 and (self.name == 'storage room' or self.name == 'the blue hallway'):
            print("The chambermaid is here, dancing to forget.")
        else:
            print("Where is the chambermaid?")

    def visit(self,count):
        answer = None
        while answer not in self.locations:

            if 'jujube' in inventory and 'caramel' in inventory and 'chocolate' in inventory and self.name == 'hotel front door':
                print("\n\nYou have all the candy and you can escape! \n"

                    "The chambermaid appears and escapes with you! You win!\n\n")
                exit(0)
            else:
                print("")

            self.describe()
            self.chambermaid()
            answer = input('Direction, unlock, or take, drop, inventory? ')
            if answer.startswith('unlock'):
                if "key" in inventory:
                    door.remove('locked')
                    door.append('unlocked')
                    self.text = ''
                    self.text = "You are standing outside a storage room."
                    self.locations['south'] = 'storage room'
                else:
                    print("You don't have the key yet to unlock the door.")

            if answer.startswith('take'):
                verb, obj = answer.split()
                if obj in self.items:
                    inventory.append(obj)
                    self.items.remove(obj)
                else:
                    print("Can't find", obj)

            if answer.startswith('drop'):
                verb, obj = answer.split()
                if obj in inventory:
                    inventory.remove(obj)
                    self.items.append(obj)
                else:
                    print("Don't have", obj)

            if answer.startswith('inventory'):
                print('Inventory:', ', '.join(inventory))
        count += 1
        new_location_string = self.locations[answer]
        new_location = locations[new_location_string]
        new_location.visit(count)

locations = {
    'lobby': Location('You are in a hotel lobby.', 
        locations={
            'west': 'east-west hallway',
            'east': 'hotel front door',
        },
        items=[
            'phone',
        ],
    ),

    HOTEL_FRONT_DOOR: Location(
        (
            "You attempt to open the lobby front door but you can't escape. \n"
            "You notice the name of the establishment is 'Hotel California'."
        ),
        locations={
            'west': 'lobby',
        },
        items=[
            'key',
        ],
        name=
        HOTEL_FRONT_DOOR,
        
    ),

    'east-west hallway': Location(
        'You are in a long hallway.',
        locations={
            'south': 'at storage room door',
            'west': 'outside Room 101',
            'east': 'lobby',
        },
        items=[
            'dustbunny',
        ],
    ),

    'at storage room door': Location(
        'You are outside the locked door to the storage room.',
        locations={
            'west': 'outside Room 101',
            'east': 'lobby',
        },
        items=[
        ],
    ),

    'storage room': Location(
    'You are in the storage room.',
        locations={
        'north': 'east-west hallway',
        },
        items=[
        'chocolate'
        ],
        name=
        'storage room',
    ),
    
    'outside Room 101': Location(
        'You are outside Room 101.',
        locations={
            'north': 'north-south hallway',
            'east': 'east-west hallway',
            'west': 'Room 101',
        },
        items=[
        ],
    ),

    'Room 101': Location(
        'You are in a hotel room with velvet wallpaper on the walls.',
        locations={
            'east': 'outside Room 101',
            'west': 'bathroom',
        },
        items=[
            'phone',
            'book',
            'caramel',
        ],
    ),

    'bathroom': Location(
        'You are in a small bathroom. Everything is sparkling clean.',
        locations={
            'east': 'Room 101',
        },
        items=[
            'toothpaste',
            'brush',
            'glass',
        ],
    ),

    'north-south hallway': Location(
        'You are in a long hallway.',
        locations={
            'north': 'outside Room 102',
            'south': 'outside Room 101',
        },
        items=[
            'dustbunny',
        ],
    ),

    'outside Room 102': Location(
        'You are outside Room 102.',
        locations={
            'north': 'Room 102',
            'east': 'the blue hallway',
            'south': 'outside Room 101',
        },
        items=[
            'dustbunny',
        ],
    ),

    'Room 102': Location(
        'You are in a hotel room with pink champagne on ice.',
        locations={
            'south': 'outside Room 102',
        },
        items=[
            'jujube',
            'beast',
            'champagne',
        ],
    ),
    
    'the blue hallway': Location(
        'You are in a long hallway.',
        locations={
            'east': 'dead end',
            'west': 'outside Room 102',
        },
        items=[
            'dustbunny'
        ],
        name=
        'the blue hallway',
    ),
    'dead end': Location(
       ( "You are at the end of a long hallway.\n"
        "Outside the window, there are lots of pretty, pretty boys dancing."),
        locations={
            'east': 'dead end',
            'west': 'outside Room 102',
        },
        items=[
            'dustbunny'
        ],
        name=
        'the blue hallway',
    ),
}




main()