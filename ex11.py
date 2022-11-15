'''Write a Python program which accepts a sequence of comma separated 4 digit binary numbers as its input and print the numbers that are divisible by 5 in a comma separated sequence. Go to the editor
Sample Data : 0100,0011,1010,1001,1100,100'''

binary = input().split(',')
binary = [int(i) for i in binary]
print(binary)
div = []
for i in binary:
    if i % 5 == 0:
        div.append(i)
print(*div, sep=',')
