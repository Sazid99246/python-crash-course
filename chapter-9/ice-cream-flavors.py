from restaurant import Restaurant

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