
text = text.strip()

HOTEL_FRONT_DOOR = 'hotel front door'

    HOTEL_FRONT_DOOR: Location(
        """
        	You attempt to open the lobby front door but you can't escape.
        	You notice the name of the establishment is 'Hotel California'.
       """,
        locations={
            'west': 'lobby',
        },
        items=[
            'key',
        ],
        name=HOTEL_FRONT_DOOR,
    ),
HOTEL_FRONT_DOOR: Location(
        (
            "You attempt to open the lobby front door but you can't escape.\n"
            "You notice the name of the establishment is 'Hotel California'."
       ),
        locations={
            'west': 'lobby',
        },
        items=[
            'key',
        ],
        name=HOTEL_FRONT_DOOR,
    ),

    villain_location = random.choice(['lobby', 'storage room'])

if villain_location == self.name:
    print('the villain is here!')



