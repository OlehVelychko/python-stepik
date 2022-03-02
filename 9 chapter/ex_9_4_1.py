# cities = input().split()
# res = filter(lambda x: len(x) > 5, cities)
# for i in range(3):
#     print(next(res), end=' ')


# import sys
#
# # считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))
#
# # здесь продолжайте программу (используйте список lst_in)
# arr = [''.join(list(x)).split('=') for x in lst_in]
# arr = [(x[0], int(x[1])) for x in arr]
# # print(arr)
#
# gen = map(tuple, arr)
# for i in gen:
#     if i[1] > 500:
#         print(i[0], end=' ')
# res = filter(lambda x: x[1] > 500, gen)
# for i in res:
#     print(i)


# import sys
#
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# tp = tuple(map(lambda s: tuple(str.split(s, sep='=')), lst_in))
# f = filter(lambda x: int(x[1]) >= 500, tp)
# gen = map(lambda x: x[0], f)
# print(*gen)


# import sys
#
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# f = filter(lambda x: int(x[1]) >= 500, tuple(map(lambda x: tuple(x.split('=')), lst_in)))
# print(*(item for item, weight in f))


# digits = map(int, input().split())
# res = filter(lambda x: 10 <= abs(x) <= 99, digits)
# for i in res:
#     print(i, end=' ')


# print(*filter(lambda x: 9 < abs(x) < 100, map(int, input().split())))

