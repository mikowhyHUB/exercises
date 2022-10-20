'''
Write a program to accept a string from the user and display characters that are present at an even index number.

For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.
'''


def even(word):
    for char in range(0, word, 2):
        print(word[char])


string = input('What word would you like to check: ')

even(string)
