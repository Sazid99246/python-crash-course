favorite_numbers = {
    "Sazid": [991, 992, 99146, 99246, 223020005],
    "Lazz": [554, 20, 14, 7],
    "Mukta": [1971, 1996, 2000, 2005],
    "Shafiq": [1967, 7404],
}

for name, numbers in favorite_numbers.items():
    print(name.title() + "likes the following numbers:")
    for number in numbers:
        print(number)