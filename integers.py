#Write a program in Python language that asks the user to enter their integer number and to display it if this number is even or odd

even_odd = int(input())

if even_odd %2 == 0:
    print('It\'s even!')
else:
    print('It\'s odd!')