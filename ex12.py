'''Write a Python program that accepts a string and calculate the number of digits and letters.'''

words = input()

l = 0
d = 0
for i in words:
    if i > 'a' or i > 'A':
        l += 1
    elif i > '0' and i < '9':
        d += 1
print('letters', l)
print('digits', d)
