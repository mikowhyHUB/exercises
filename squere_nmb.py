'''
Write a Python function to create and print 
a list where the values are square of numbers 
between 1 and 30 (both included).
'''
l = []
for i in range(1, 31):
    i *= i
    l.append(i)
print(l)
