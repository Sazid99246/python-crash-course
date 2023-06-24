guests = ["Hira", "eldest aunt", "shahin"]
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
