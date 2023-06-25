my_pizzas = ["Margherita Pizza", "Chicken Sausage Pizza", "Chicken Fiesta Pizza"]
friends_pizzas = my_pizzas[:]
my_pizzas.append("Buffalo Chicken Pizza")
friends_pizzas.append("Grandma Pizza")
print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friends_pizzas:
    print(pizza)