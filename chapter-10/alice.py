def count_words(filename):
    try:
        with open(filename, encoding='utf-8') as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")

filenames = ['txt_files/alice.txt', 'txt_files/siddhartha.txt', 'txt_files/moby_dick.txt', 'txt_files/little_women.txt']
for filename in filenames:
    count_words(filename)