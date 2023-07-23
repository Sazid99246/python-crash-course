def city_country(city, country, population = ''):
    if population:
        return f"{city.title()}, {country.title()} - {str(population)}"
    else:
        return f"{city.title()}, {country.title()}"