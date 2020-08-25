
ramit = {
    'name': 'ramit',
    'email': 'ramit@gmail.com',
    'interests': ['movie', 'tennis'],
    'friends': [
        {
            'name': 'Jasmine',
            'email': 'jasmine@yahoo.com',
            'interests': ['photography', 'tennis']
        },
        {
            'name': 'Jan',
            'email': 'jasmaine@yahoo.com',
            'interests': ['movies', 'tv']
        }
    ]
}

print(ramit['email'])
print(ramit['interests'][0])


friends_email = ramit['friends'][0]['email']
print(friends_email)


friends_interests = ramit['friends'][1]['interests']
print(friends_interests)
