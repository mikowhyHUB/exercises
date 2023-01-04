# Write a program in Python that asks the user to enter 5 integers of their choice and display the list of numbers entered.

integers = input('enter 5 integers separeted with coma:').split(',')
test = [int(i) for i in integers]

print(test)
