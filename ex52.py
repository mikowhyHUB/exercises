'''
Generate a Python list of all the even numbers between 4 to 30
'''


def even(num):
    out = [i for i in range(4, num+1) if i % 2 == 0]
    print(out)


even(30)
