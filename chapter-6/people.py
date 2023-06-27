people = {
    'yakub': {
        'first_name': 'yakub',
        'last_name': 'hossain',
        'age': 22,
        'city': 'dhaka'
    },
    'jilani': {
        'first_name': 'abdul kader',
        'last_name': 'jilani',
        'age': 24,
        'city': 'khulna'
    },
    'ripon': {
        'first_name': 'ismail hossain',
        'last_name': 'ripon',
        'age': 22,
        'city': 'rajshahi'
    }
}

for person, person_details in people.items():
    full_name = person_details['first_name'] + " " + person_details['last_name']
    print("\nFull name: " + full_name.title())
    print("Age: " + str(person_details['age']))
    print("City: " + person_details['city'].title())