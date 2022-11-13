'''Write a Python program that accepts a word from the user and reverse it.'''

word = list(input('What word would you like to reverse: '))
word.reverse()
word = [print(i, end='') for i in word]
