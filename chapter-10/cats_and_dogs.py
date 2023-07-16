filenames = ['txt_files/cats.txt', 'txt_files/dogs.txt']

for filename in filenames:
    try:
        with open(filename) as file:
            print(f"Reading files {filename}")
            contents = file.read()
            print(contents + "\n")

    except FileNotFoundError:
        pass