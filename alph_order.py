'''Write a Python program that accepts 
a hyphen-separated sequence of words 
as input and prints the words in a hyphen-separated sequence after 
sorting them alphabetically. Go to the editor
Sample Items : green-red-yellow-black-white
Expected Result : black-green-red-white-yellow
'''


def sequence(income):
    outcome = income.split('-')
    for i in outcome:
        outcome.sort()
    print('-'.join(outcome))


sequence('green-red-yellow-black-white')
