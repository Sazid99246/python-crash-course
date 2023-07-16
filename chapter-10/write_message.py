filename = 'txt_files\programming.txt'

with open(filename, 'w') as file_object:
    file_object.write('I write programming. \n')
    file_object.write('I like creating new games. \n')

with open(filename, 'a') as file_object:
    file_object.write('I also love finding meaning in large datasets. \n')
    file_object.write('I love creating apps that can run in the browser. \n')