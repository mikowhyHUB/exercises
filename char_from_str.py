# podane słowo musisz wydrukować tylko te co są parzyste.
# Wylicz długość słowa, sprawdzic czy inex jest parzysty, wydrukowac tylko te litery parzyste


x = input("Enter String: ")
print('Original String is ', x)
print('Printing only even index chars')
for i in range(len(x)):
    if i % 2 == 0:
        print(x[i])
