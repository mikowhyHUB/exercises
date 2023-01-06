def hello():
    print('Hello')


def pretty_print(func):
    def wrapper():
        print('=' * 30)
        func()
        print('=' * 30)
    return wrapper


hello = pretty_print(hello)
hello()
