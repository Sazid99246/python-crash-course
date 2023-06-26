# 1
name = "John"
print("Is his name John? I predict True.")
print(name == "John")

# 2
print("\nIs his name Don? I predict False.")
print(name == "Don")

# 3
book = "Python Crash Course"
print("\nWhat are you reading? Python Crash Course? I predict True")
print(book == "Python Crash Course")

# 4
print("\nWhat are you reading? Python For Everybody? I predict False")
print(book == "Python For Everybody")

# 5
car = 'subaru'
print("\nIs car == 'subaru'? I predict True.")
print(car == 'subaru')

# 6
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

# 7
food = "pizza"
print("\nCan you guess what I am eating now? I predict True.")
print(food == "pizza")

# 8
print("\nCan you guess what I ate last night? I predict False.")
print(food == "Sandwich")

# 9
sleeping_time = "10pm"
print("\nCan you guess when I went to sleep yesterday? I predict True.")
print(sleeping_time == "10pm")

# 10
print("\nCan you guess when I went to sleep the day before yesterday? I predict False.")
print(sleeping_time == "2am")


# more tests

print("\nequality and inequality with strings")
print("abc" == "abc")
print("abc" == "def")

print("\nusing the lower() function")
print("Sazid".lower() == "sazid")
print("Sazid" == "sazid")

print("\nNumerical tests involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to")
print(5 == 5)
print(5 == 7)
print(6 > 5)
print(5 > 6)
print(20 >= 10)
print(20 >= 40)
print(30 < 40)
print(30 < 10)
print(30 <= 30)
print(30 <= 20)

print("\nTests using the and keyword and the or keyword")
print(5 > 2 and 100 > 20)
print(5 > 2 and 20 > 100)
print(2 > 5 and 20 > 100)
print(2 > 5 and 100 > 20)
print(5 > 2 or 100 > 20)
print(5 > 2 or 20 > 100)
print(2 > 5 or 20 > 100)
print(2 > 5 or 100 > 20)

print("\nTest whether an item is in a list")
names = ["Sazid", "Lazz", "Mukta", "Shofiqul"]
if "Sazid" in names:
    print(True)
    print("Hi, Sazid is here")

print("\nTest whether an item is not in a list")
if "Asif" not in names:
    print(False)
    print("Sorry, Asif couldn't come today")