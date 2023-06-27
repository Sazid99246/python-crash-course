favorite_places = {
    'eric': ['bear mountain', 'death valley', 'tierra del fuego'],
    'erin': ['hawaii', 'iceland'],
    'willie': ['mt. verstovia', 'the playground', 'new hampshire']
}

for name, places in favorite_places.items():
    print(name.title() + " likes the following places:")
    for place in places:
        print(place.title())