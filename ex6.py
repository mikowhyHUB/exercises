'''
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.'''
from math import sqrt

def calculate(num):
    return sqrt((2* 50 * num)/30)

num = input('Enter numbers separeted with coma: ').split(',')
num = [int(i) for i in num]

q = [calculate(i) for i in num]
q = [round(i) for i in q]
q = [str(i) for i in q]
print(','.join(q))