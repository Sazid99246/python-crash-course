with open("txt_files\learning_python.txt") as pythonlearn:
    lines = pythonlearn.readlines()
    for line in lines:
        print(line.strip().replace("Python", "C"))
