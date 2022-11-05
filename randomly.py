import random

def random_list(l):
    random.shuffle(l)
    return l

l1 =[1,'cat',45,'sword',420]
print(random_list(l1))