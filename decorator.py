from functools import wraps


def header(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print('<h1>')
        func(*args, **kwargs)
        print('</h1>')

    return inner


def table(func):
    def inner(*args, **kwargs):
        print('<table>')
        func(*args, **kwargs)
        print('</table>')

    return inner

@header
def sqrt(x):
    """
    :param x:
    Inputting an integer number
    :return:
    The function is printing square of X
    """
    print(x ** 2)


@table  # say = table(header(say))
@header  # say = header(say)
def say(name, surname, age):
    print('Hello', name, surname, age)


sqrt(7)
