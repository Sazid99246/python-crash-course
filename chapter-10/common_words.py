files = ['txt_files/the_haunter_of_the_ring.txt', 'txt_files/father_tom_and_pope.txt', 'txt_files/tarzan.txt']


for file in files:
    with open(file, encoding='utf-8') as text:
        contents = text.read()
        count_the = contents.lower().count('the')
        print("\nThe text " + file.title() + "repeats the word 'the' for " + str(count_the) + " times")