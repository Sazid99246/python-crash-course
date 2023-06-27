cities = {
    'santiago': {
        'country': 'chile',
        'population': 6_310_000,
        'nearby-mountains': 'andes',
    },
    'talkeetna': {
        'country': 'united states',
        'population': 876,
        'nearby-mountains': 'alaska range',
    },
    'kathmandu': {
        'country': 'nepal',
        'population': 975_453,
        'nearby-mountains': 'himilaya',
    }
}

for city, city_info in cities.items():
    country = city_info['country'].title()
    population = str(city_info['population'])
    mountains = city_info['nearby-mountains']
    print("\n" + city.title() + " is in " + country + ".")
    print("It has a population about" + population + ".")
    print("The " + mountains.title() + " are nearby.")