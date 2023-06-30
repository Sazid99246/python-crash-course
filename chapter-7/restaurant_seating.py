message = input("How many people are you in your group? ")
message = int(message)

if message > 8:
    print("Sorry, you have to wait for some more time for a table!")
else:
    print("Welcome, your table is ready!")