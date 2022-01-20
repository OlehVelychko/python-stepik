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

d = {}
a = int(input())
while a != 0:
    if a not in d:
        print(round((a ** 0.5), 2))
        d[a] = a ** 0.5
    else:
        print(f'значение из кэша: {d[a]}')
    a = int(input())
