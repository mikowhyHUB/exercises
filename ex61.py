a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


def list_less_then():
    for item in a:
        if item < 5:
            x = []
            x.append(item)
            print(x)


list_less_then()
