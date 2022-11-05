def two_lists(a,b):
    l = []
    for i in a:
        if i in b:
            l.append(i)
    return l
    
    
l1= [1,2,3,4]
l2= [3,4,5,6]
print(two_lists(l1,l2))
