guests = ["hira", "eldest aunt", "shahin"]
print(guests[0].title() + ", you are invited to our dinner, today")
print(guests[1].title() + ", you are invited to our dinner, today")
print(guests[2].title() + ", you are invited to our dinner, today")

not_attendable = guests[1].title()
print(not_attendable.title() + " can't join the dinner because of sickness")

del(guests[1])
guests.insert(1, "liton")
print(guests)
print("Instead of " + not_attendable.title() + ", " + guests[1].title() + " will attend the dinner.")
print(guests[0].title() + ", you are invited to our dinner, today")
print(guests[1].title() + ", you are invited to our dinner, today")
print(guests[-1].title() + ", you are invited to our dinner, today")

print("Guys, I found a bigger dining table. Now, I want to invite others to join the dinenr.")

guests.insert(0, "rikta")
guests.insert(0, "lakhi")
guests.append("imran")
print(guests)
print(guests[0].title() + ", you are invited to our dinner, today")
print(guests[1].title() + ", you are invited to our dinner, today")
print(guests[2].title() + ", you are invited to our dinner, today")
print(guests[3].title() + ", you are invited to our dinner, today")
print(guests[4].title() + ", you are invited to our dinner, today")
print(guests[5].title() + ", you are invited to our dinner, today")

print("I am sorry. As the table wo't arrive at the time, I have to eliminate some of you.")
deleted_guest = guests.pop()
print(deleted_guest.title() + " ,you are eliminated")
deleted_guest = guests.pop()
print(deleted_guest.title() + " ,you are eliminated")
deleted_guest = guests.pop()
print(deleted_guest.title() + " ,you are eliminated")
deleted_guest = guests.pop()
print(deleted_guest.title() + " ,you are eliminated")

remaining_guest = guests[0]
print("Congratulations, " + remaining_guest.title() + "! You are remaining till now!")
remaining_guest = guests[1]
print("Congratulations, " + remaining_guest.title() + "! You are remaining till now!")

del guests[0]
del guests[0]
print(guests)
