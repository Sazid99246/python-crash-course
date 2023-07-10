from restaurant import Restaurant

restaurant = Restaurant("the mean queen", "pizza")
print(restaurant.restaurant_name.title())
print(restaurant.cuisine_type)
print(restaurant.number_served)
restaurant.number_served = 20
print(restaurant.number_served)
restaurant.set_number_served(50)
print(restaurant.number_served)
restaurant.increment_number_served(20)
print(restaurant.number_served)

restaurant.describe_restaurant()
restaurant.open_restaurant()

mean_queen = Restaurant('the mean queen', 'pizza')
mean_queen.describe_restaurant()

ludvigs = Restaurant("ludvig's bistro", 'seafood')
ludvigs.describe_restaurant()

mango_thai = Restaurant('mango thai', 'thai food')
mango_thai.describe_restaurant()