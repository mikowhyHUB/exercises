from curses.ascii import isdigit
import random

top_of_range = input('Type a number: ')

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('Type only numbers larger than 0.')
        quit()
else:
    print('Please type a number next time.')
    quit()

random_number = random.randint(0, top_of_range)

while True:
