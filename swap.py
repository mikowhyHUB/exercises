# write python algorithm to swap the first element with the last element of given list.
l = ["Python", "Java", "C++", "Javascript"]


def swap(list):
    swap = list[-1]
    list[-1] = list[0]
    list[0] = swap
    return list


print(swap(l))
