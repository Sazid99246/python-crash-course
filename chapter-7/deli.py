sandwich_orders = ["club", "pastrami", "tuna", "reuben", "cubano", "pastrami", "italian", "capress", "pastrami"]
finished_sandwiches = []

print("The deli has run out of pastrami!")
while sandwich_orders:
    while 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')
    taken_sandwich = sandwich_orders.pop()
    print("I made your " + taken_sandwich.title() + " Sandwich.")
    finished_sandwiches.append(taken_sandwich)

print("The following sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(sandwich.title() + " Sandwich.")