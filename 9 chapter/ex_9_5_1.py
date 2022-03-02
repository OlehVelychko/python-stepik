# # arr1 = list(map(int, input().split()))
# # arr2 = list(map(int, input().split()))
# #
# # res = zip(arr1, arr2)
# # a = []
# # for x in res:
# #     a.append(x[0] * x[1])
# #     # print(x[0] * x[1])
# #
# # for i in range(3):
# #     print(a[i], end=' ')
#
#
# # s1 = map(int, input().split())
# # s2 = map(int, input().split())
# # result = map(lambda x: x[0] * x[1], zip(s1, s2))
# # for el in range(3):
# #     print(next(result), end=" ")
#
# # a = map(int, input().split())
# # b = map(int, input().split())
# #
# # mult = map(lambda x: x[0] * x[1], zip(a, b))
# #
# # print(*(next(mult) for i in range(3)))
#
#
# lst_in = [
#     [1, 2, 3, 4, 5, 6],
#     [3, 4, 5, 6],
#     [7, 8, 9],
#     [9, 7, 5, 3, 2]
# ]
#
# # res = zip(arr)
# # print(*res)
#
# a = []
# for x in lst_in:
#     a.append(len(x))
#     # for j in x:
#     #     print(j, end=' ')
#     # print()
# # print(a)
# m = min(a)
# # print(m)
# s = ''
# for x in lst_in:
#     for j in range(m):
#         s += str(x[j])
#     print(s)
#     s = ''
#     # print()


# import sys
#
# # считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))
#
# for i in zip(*zip(*lst_in)):
#     print(*i, sep='')


# import sys
#
# # считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))
#
# # здесь продолжайте программу (используйте список строк lst_in)
#
# lst_in = [list(map(int, x.split())) for x in lst_in]
# # скармливаем zip нашу распакованную матрицу
# res = [list(row) for row in zip(*lst_in)]
# # из-за того, что в процессе матрицу повернуло, траснпонируем ее еще раз
# for row in zip(*res):
#     print(*row)


# res = zip(*[iter(input().split())]*3)
# for x in res:
#     print(*x)

# s = input()
# numbers = list(range(len(s)))
#
# lst = list(zip(s, numbers)) if len(numbers) < 10 else list(zip(s, numbers[:10]))
# # for x in lst:
# #     print(x)
# # print(numbers)
# print(lst)


# s = input()
#
# lst = list(zip(s, range(10)))