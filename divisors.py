#Write a Python algorithm that returns the list of divisors of a given integer. Example if n = 18, the algorithm returns the list [1, 2, 3, 6, 9, 18]

def divisors(num):
    l=[]
    for i in range(1, num+1):
        if num%i == 0:
            l.append(i)
    print(l)

divisors(18)