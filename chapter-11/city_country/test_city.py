from city_country import city_country

def test_city_country():
    formatted_country = city_country("dhaka", "bangladesh")
    assert formatted_country == "Dhaka, Bangladesh"

def test_city_country_population():
    formatted_country = city_country("dhaka", "Bangladesh", 20000000)
    assert formatted_country == "Dhaka, Bangladesh - 20000000"