def common_element(a,b):
    if a in b:
        return True
    else:
        return False
    
    
list1 = [1,2,3,4,5,6]
list2 = [6,7,8,9]

print(common_element(list1,list2))