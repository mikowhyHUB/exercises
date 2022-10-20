from asyncore import write


with open('test.txt') as old_file:
    lines = old_file.readlines()


with open('new_file.txt', mode='w') as new_file:
    counter = 0
    for i in lines:
        if counter == 4:
            counter += 1
            continue
        else:
            new_file.write(i)
        counter += 1
