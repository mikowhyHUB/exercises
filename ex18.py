'''Write a Python program to read first n lines of a file.'''


def read_lines(file, lines):
    txt = open(file)
    for i in range(lines):
        print(txt.readline())


read_lines('text.txt', 3)
