import json

filename = 'json_files/favorite_number.json'
try:
    with open(filename) as file_obj:
        number = json.load(file_obj)

except FileNotFoundError:
    n = input("Write your favorite number: ")
    with open(filename, 'w') as file_obj:
        json.dump(n, file_obj)
        print("Thanks, I will remember that")

else:
    print(f"I know your favorite number! It's {number}.")