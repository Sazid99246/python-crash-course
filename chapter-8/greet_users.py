def greet_users(names):
    """Prints a greeting to each users in the list"""
    for name in names:
        message = "Hello, " + name + "!"
        print(message)

greet_users(['hannah', 'ty', 'margot'])