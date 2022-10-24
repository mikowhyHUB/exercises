'''
Write a program to use the loop to find the factorial of a given number.
'''
count = 1
for i in range(1, 6):
    i = count * i
    count = i
    print(count)
