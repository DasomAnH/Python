hotels = [{
    '101': {
        'guest': {
            'name': 'Elliot Alderson',
            'phone': 8675309
        }
    },
    '102': {},
    '103': {},
    '104': {
        'guest': {
            'name': 'Darlene Alderson',
            'phone': 4567890
        }
    },
    '105': {},
},
    {
    '101': {
        'guest': {
            'name': 'Elliot Alderson',
            'phone': 8675309
        }
    },
    '102': {},
    '103': {},
    '104': {
        'guest': {
            'name': 'Darlene Alderson',
            'phone': 4567890
        }
    },
    '105': {},
},
    {
    '101': {
        'guest': {
            'name': 'Elliot Alderson',
            'phone': 8675309
        }
    },
    '102': {},
    '103': {},
    '104': {
        'guest': {
            'name': 'Darlene Alderson',
            'phone': 4567890
        }
    },
    '105': {},
}
]


def is_vacant(hotel, room_number):
    # add an if-the-room-exists loop
    # because of how Python treats Falsey key values like errors, we need to only work with Truthy key-values
    try:
        # if there is a value here, it's because there's a guest staying there!
        if hotel[room_number]:
            #print("Hotel room is full")
            return False
        else:
            #print("Hotel room is empty.")
            return True
            # it's not empty, so is-vacant/is-empty is false, basically
    except KeyError:
        # this gets around the error thrown when Python deals with a Falsey key-value - an empty room.
        #print("Hotel room non-existant.")
        return False
        # it is empty so we return true


def check_in(hotel, room_number, guest_name):
    # if that room number is empty
    if is_vacant(hotel, room_number) == True:
        # assign our guest to it
        hotel[room_number] = guest_name
        return hotel
    else:
        #print("Nope, no room here")
        return hotel


def check_out(hotel, checkoutroom):
    # replaces anything in the key-value (room) with nothing (an empty dictionary)
    hotel[checkoutroom] = {}
    # this sends back the modified hotel list
    return hotel


while True:
    # this should print a list of empty rooms
    emptyrooms = []
    for hotel in hotels:
        for room in hotel.keys():
            if is_vacant(hotel, room):
                emptyrooms.append(room)
    print(f'These {emptyrooms} are empty.')
    # this should ask you which empty room you want to stay in

    # checkin block - grabs user info and uses that to find them a room
    checkin_name = input("What's your name? ")
    checkin = input("Which room would you like? ")
    hotelnum = int(input("Would you like to stay in hotel 1, 2, or 3? "))
    check_in(hotels[hotelnum - 1], checkin, checkin_name)
    print(hotels[hotelnum - 1])

    checkout = input("Which room are you vacating? ")
    hotelnum = int(input("Are you checking out of hotel 1, 2, or 3? "))
    check_out(hotels[hotelnum - 1], checkout)
    print(hotels[hotelnum])

    quitinput = input(
        "Are you finished booking today? [UI improvements by Alison] ")
    if quitinput == "yes":
        break
    else:
        checkin_name = input("Would you like to check into another room? ")
        break
