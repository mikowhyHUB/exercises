from curses.ascii import isdigit


def when_100yo():
    name = input("What is your name? ")
    age = input("What is your age? ")
    if age.isdigit():
        year = 100 - int(age) + 2022
        if year < 2022:
            print("Damn you old!")
        else:
            print("Hi,", name, "the year you will turn 100 years old would be", year)
    else:
        print("You need to enter your age. Try again")
        return when_100yo()


when_100yo()
