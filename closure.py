# def counter():
#     count = 0
#
#     def adder():
#         nonlocal count
#         count += 1
#         return count
#
#     return adder
#
# closure = counter()
# for _ in range(20):
#     print(closure())


# def average():
#     numbers = []
#
#     def inner(number):
#         numbers.append(number)
#         print(numbers)
#         return sum(numbers) / len(numbers)
#
#     return inner
#
#
# a1 = average()
# print(a1(10))
# print(a1(5))
# print(a1(6))
# b1 = average()
# print(b1(12))
# print(b1(18))
# print(b1(25))
# print(a1(55))
# print(b1(77))
# print(a1(5) + b1(10))


def adder(a, b):
    return a + b


def counter(func):
    count = 0

    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print(f'{func.__name__} has been called {count} times')
        return func(*args, **kwargs)

    return inner


q = counter(adder)
print(q(10, 20))
print(q(40, 50))
