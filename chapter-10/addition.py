while True:
    try:
        a = input("Write a number: ")
        if a == "q":
            break
        a = int(a)

        b = int(input("Write another number: "))
        b = int(b)
    
    except ValueError:
        print("Please write a number")

    else:
        print(a + b)