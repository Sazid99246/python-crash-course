users = ["Sazid", "Lazz", "admin", "Mukta", "Liton"]
new_users = ["Jahid", "Promish", "Sazid", "Mukta", "Nitu"]
for new_user in new_users:
    if new_user in users:
        print("Sorry, the username, " + new_user + " has picked by someone else. Please enter a new username.")
    else:
        print(new_user + " is available.")
