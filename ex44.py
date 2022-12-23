'''Take a nested list and return a single flattened list with all values except nil/null.

The challenge is to write a function that accepts an arbitrarily-deep nested list-like structure and returns a flattened structure without any nil/null values.

For example:

input: [1,[2,3,null,4],[null],5]

output: [1,2,3,4,5]'''


def flatten(iterable):
    output = []
    for num in iterable:
        if type(num) is int:
            output.append(num)
        elif type(num) is list:
            output += flatten(num)
    return output


inputs = [0, 2, [[2, 3], 8, 100, 4, [[[50]]]], -2]
expected = [0, 2, 2, 3, 8, 100, 4, 50, -2]
print(flatten(inputs))
