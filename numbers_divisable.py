'''
Iterate the given list of numbers and print only those numbers which are divisible by 5
'''


def given_list(lst):
    for num in lst:
        if num % 5 == 0:
            print(num)


lst = [10, 20, 33, 46, 55]
given_list(lst)
