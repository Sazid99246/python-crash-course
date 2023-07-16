with open("txt_files\learning_python.txt") as pythonlearn:
    lines = pythonlearn.readlines()
    for num in range(3):
        for line in lines:
            print(line.strip())
        print("----------------------------------------")
        print("\n")
 


with open("txt_files\learning_python.txt") as pythonlearn:
    lines = pythonlearn.readlines()
    pi_string = ''
    for line in lines:
        for n in range(3):
            pi_string += line.strip()

print(pi_string)
print(len(pi_string))