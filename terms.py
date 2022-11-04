#Write an algorithm in python that returns the average of the terms in a list of numbers
def average(l):
    n = len(l)
    l = sum(l)
    x = l/n
    print(x)

l = [3,7,8,2]

average(l)