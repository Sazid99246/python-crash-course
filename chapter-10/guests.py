while True:
    guest = input("Write your name: ")
    if guest == 'done':
        break
    with open('txt_files\guest_book.txt', 'a') as file_object:
        file_object.write(guest + '\n')