from datetime import timedelta


def add(moment):
    delta = timedelta(seconds=10**9)
    return moment + delta


print(add(2011, 4, 25, 0, 0))
