# import math
#
# d = {}
# a = []
# n = int
# while n:
#     n = int(input())
#     a.append(n)
#
#     for i in range(len(a)):
#         key = a[i]
#         value = round(math.sqrt(key), 2)
#         d[key] = value
#
# w = float
# for i in d.values():
#     print(i)
#     w = i
#     continue
#
#     if i == w:
#         print('значение из кэша:', i)
#     # else:
#     # print(i)
#     # w = i
#
# # print(d)

# lst =[]
# d = {}
# a = int(input())
# while a != 0:
#     if a not in d:
#         # print(round((a ** 0.5), 2))
#         d[a] = a ** 0.5
#         lst.append(round(d[a], 2))
#     else:
#         lst.append(f'значение из кэша: {round(d[a], 2)}')
#     a = int(input())
#
# for x in lst:
#     print(x)


# n = int(input())
# d = {}
#
# while n != 0:
#     if n in d:
#         print(f'значение из кэша: {d[n]}')
#     else:
#         d[n] = round(n ** .5, 2)
#         print(d[n])
#     n = int(input())


# n = int(input())
# d = {}
# while n != 0:
#     if d.get(n):
#         print(f'значение из кэша: {d[n]}')
#     else:
#         d[n] = round(n ** 0.5, 2)
#         print(d[n])
#     n = int(input())


import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)
# d = {}
# for x in lst_in:
#     if x in d:
#         d[x] = x
#         print(f"Взято из кэша: HTML-страница для адреса {d[x]}")
#     else:
#         d[x] = x
#         print(f"HTML-страница для адреса {d[x]}")



