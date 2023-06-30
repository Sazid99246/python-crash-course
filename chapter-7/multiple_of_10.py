number = input("Enter a number, and I will tell you if the number is a multiple of 10 or not: ")
number = int(number)
if number % 10 == 0:
    print(str(number) + " is a multiple of 10.")
else:
    print(str(number) + " is not a multiple of 10.")