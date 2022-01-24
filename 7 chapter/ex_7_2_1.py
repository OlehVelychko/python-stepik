# def get_square(x):
#     res = x ** 2
#     return res
#
#
# a = float(input())
# print(get_square(a))


# def is_triangle(a, b, c):
#     return (a + b) > c and (a + c) > b and (b + c) > a
#
#
# x, y, z = map(int, input().split())
# print(is_triangle(x, y, z))


# def is_large(s):
#     return len(s) >= 3
#
#
# s = input()
# print(is_large(s))


# def get_even(x):
#     return not x % 2
#
#
# a = int
# m = []
#
# while a != 1:
#     a = int(input())
#     if get_even(a):
#         m.append(a)
# for x in m:
#     print(x)


def is_even(n):
    return not n % 2


n = int(input())

while n != 1:
    if is_even(n):
        print(n)
    n = int(input())