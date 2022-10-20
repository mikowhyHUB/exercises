'''
Write a program to iterate the first 10 numbers and in each iteration, print the sum of the current and previous number.
'''

prev = 0
for i in range(10):
    prev = i - 1
    sum = i+prev
    print('current number', i, 'previus number:', prev, 'sum', sum)
