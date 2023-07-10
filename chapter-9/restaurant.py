class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("\nThis is " + self.restaurant_name.title() + ".")
        print("We serve " + self.cuisine_type)
    
    def open_restaurant(self):
        print(self.restaurant_name.title() + " is open now. Come on in.")

    def set_number_served(self, number_served):
        self.number_served = number_served
    
    def increment_number_served(self, additional_served):
        self.number_served += additional_served

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

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def displayFlavors(self):
        print("We sell ice-creams of the flavors below:")
        for flavor in self.flavors:
            print(" -" + flavor.title())

new_icecream = IceCreamStand("Ice Cream Stand", "ice-cream", ["vanila", "chocolate", "strawberry", "coconut"])
new_icecream.displayFlavors()