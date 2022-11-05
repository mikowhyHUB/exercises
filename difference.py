def difference(a,b):
    diff_list = []
    diff_list = [i for i in a if i not in b]
    return diff_list
    
            

l1 = [11, 3, 22, 7, 13, 23, 9] 
l2 = [5, 9, 19, 23, 10, 23, 13]
print(difference(l1,l2))

