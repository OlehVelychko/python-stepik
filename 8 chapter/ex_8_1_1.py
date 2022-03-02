# import math
# a = float(input())
# print(math.ceil(a))


# from math import floor
# a = float(input())
# print(floor(a))


from math import factorial as fac


# def factorial(n):
#     p = 1
#     for i in range(2, n+1):
#         p *= i
#
#     print("my factorial")
#     return p


from random import seed, random as rnd
seed(10)
print(round(rnd(), 2))