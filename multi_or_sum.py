'''
Given two integer numbers return their product only if the product is equal to or lower than 1000, else return their sum.
'''


def numbers(num1, num2):
    if num1 * num2 <= 1000:
        print(num1*num2)
    else:
        print(num1+num2)


numbers(20, 30)
numbers(40, 30)
