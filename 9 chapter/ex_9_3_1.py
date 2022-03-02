# gen = map(float, input().split())
#
# for x in range(3):
#     print(next(gen), end=' ')


# numbers = list(map(float, input().split()))
# print(*numbers[:3])


# stroka = input()
# gen = map(lambda x: abs(int(x)), stroka.split())
# for i in gen:
#     print(i, end=' ')


import sys

# # считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))
#
# # здесь продолжайте программу (используйте список lst_in)
# # переменную lst_in не менять!
#
# # gen = map(x for x in lst_in, lst_in)
# # for i in gen:
# #     print(i, end=' ')
#
# ar = [list(x) for x in lst_in]
# print(ar)
# lst2D = map(int, ar)
# for i in lst2D:
#     print(i)

# lst_in = ['8 11 -5', '3 4 10', '-1 -2 3', '4 5 6']
# lst2D = [x.split() for x in lst_in]
#
# for x in lst2D:
#     for i, item in enumerate(x):
#         x[i] = int(item)
# print(lst2D)

# lst2D = [list(map(int, i.split())) for i in lst_in]
#
# lst2D = list(map(lambda lst: list(map(int, lst.split())), lst_in))


