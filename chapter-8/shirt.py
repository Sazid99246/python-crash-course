def make_shirt(size, message = "I love Python"):
    print("I am going to make a " + size + "shirt.")
    print("It will say " + message.title())

make_shirt("large")

make_shirt(message="Readability counts!", size="large")