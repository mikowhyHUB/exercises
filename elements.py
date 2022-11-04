#Write an algorithm in python as a function which takes as a parameter a tuple (L, x) formed by a list L and an element x and which returns the position of the element x in the list L. The function must return -1 if element x is not in the list.
def algorithm(a,b):
    if b in a:
        return a.index(b)
    else:
        return -1

l = [1,2,3]
x = 4

print(algorithm(l,x))

x = input(':')
print(x)