l = [2,4,5,2,2,4,645,43,6]

new_list = []
# new_list = [i for i in l if i not in new_list]
for i in l:
    if i not in new_list:
        new_list.append(i)
print(new_list)

