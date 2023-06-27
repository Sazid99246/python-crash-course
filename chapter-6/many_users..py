users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris'
    },
}

for usesrname, user_info  in users.items():
    print("\nUsername: " + usesrname)
    full_name = user_info['first'] + " " + user_info['last']
    locaton = user_info['location']
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + locaton.title())