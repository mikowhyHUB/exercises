'''Write a Python program to append text to a file and display the text.'''


def file_append(file):
    txt = open(file, mode='r+')
    txt.write('Python exercises')
    print(txt.read())


file_append('text.txt')
