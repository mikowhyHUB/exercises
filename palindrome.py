'''
Write a program to check if the given number is a palindrome number.

'''


def palindrome(given):
    print('Original number:', given)
    rev = 0
    while given > 0:
        last = given % 10
        rev = (rev*10) + last
        given = given // 10

    if given == rev:
        print('Yes, given number is palindrome number')
    else:
        print('No, given number is not palindrome number')


palindrome(121)
palindrome(125)
