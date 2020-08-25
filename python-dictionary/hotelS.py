hotel = {
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


def check_out(checkoutroom):
    # replaces anything in the key-value (room) with nothing (an empty dictionary)
    hotel[checkoutroom] = {}
    # this sends back the modified hotel list
    return hotel

# is_vacant takes one argument to check if a key-value (room) is empty


def is_vacant(room_number):
    # add an if-the-room-exists loop
    # because of how Python treats Falsey key values like errors, we need to only work with Truthy key-values
    try:
        # if there is a value here, it's because there's a guest staying there!
        if hotel[room_number] == True:
            print("Hotel room is full")
            return False
        else:
            print("Hotel room is empty.")
            return True
            # it's not empty, so is-vacant/is-empty is false, basically
    except KeyError:
        # this gets around the error thrown when Python deals with a Falsey key-value - an empty room.
        print("Hotel room non-existant.")
        return False
        # it is empty so we return true


print(is_vacant('107'))


def check_in(room_number, guest_name):
    # if that room number is empty
    if is_vacant(room_number) == True:
        # assign our guest to it
        hotel[room_number] = guest_name
        return hotel
    else:
        print("Nope, no room here")
        return hotel


check_out('101')

mary = {"Mary Englewood": ['phone number', 'allergies']}

print(is_vacant('101'))
print(check_in('102', mary))
print(hotel['102'])
