''' 

If we list all the natural numbers below 20 that are multiples of 3 or 5, we get 3, 5, 6, 9, 10, 12, 15, and 18.

The sum of these multiples is 78.

You can make the following assumptions about the inputs to the sum_of_multiples function:

All input numbers are non-negative ints, i.e. natural numbers including zero.
A list of factors must be given, and its elements are unique and sorted in ascending order.'''


def sum_of_multiples(limit, multiples):
    # outcome = 0
    # for num in multiples:
    #     for i in range(1, limit+1):
    #         if (num * i) < 20:
    #             outcome += num * i
    # print(outcome)
    return sum({(num * i)for num in multiples for i in range(1, limit+1)if (num * i) < limit})

    # outcome = 0
    # for num in range(1, limit+1):
    #     if (multiples[0] * num) < 20 and (multiples[0] * num) < 20:
    #         print(multiples[0] * num)
    # return outcome


print(sum_of_multiples(1, [3, 5]))
