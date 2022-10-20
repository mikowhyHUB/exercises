import random


def run_guess(guess, answer):
    if 0 < guess < 11:
        if guess == answer:
            print('Good job!')
            quit()
    else:
        print('Only number 1-10')


if __name__ == '__main__':
    answer = random.randint(1, 10)
    while True:
        try:
            guess = int(input('Chose number from 1-10: '))
            run_guess(guess, answer)

        except ValueError:
            print('please enter a number')
            continue
