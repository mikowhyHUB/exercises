# Write a Python algorithm that returns the length of a given list without using the len() method.

def length(given):
    leng = 0
    for i in given:
        leng += 1
    print(leng)


l = [1, 'dwa', 4, 123131231, 5, 'elo']
length(l)
