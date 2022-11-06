'''With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8'''

num = 8
new_dic = {}

for i in range(1, num+1):
    new_dic.update({i: i*i})
print(new_dic)