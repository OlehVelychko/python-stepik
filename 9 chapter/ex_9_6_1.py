# s = input()
# lst = list(map(int, s.split()))
# tp_lst = tuple(lst)
# # print(lst)
# # print(tp_lst)
#
# lst.sort()
# # print(lst)
# tp_lst = tuple(sorted(tp_lst))
# # print(tp_lst)


# d = {'cat': 'кот', 'horse': 'лошадь', 'tree': 'дерево', 'dog': 'собака', 'book': 'книга'}
#
#
# def get_sort(slovar):
#     a = [x[1] for x in sorted(slovar.items(), reverse=True)]
#     return a
#
#
# res = get_sort(d)
# print(res)
# for x in res:
#     print(x[1], end=' ')

# arr = set(map(int, input().split()))
#
# big = sorted(arr, reverse=True)
# for i in range(4):
#     print(big[i], end=' ')


# arr1 = map(int, input().split())
# arr2 = map(int, input().split())
# res = (x + y for x, y in zip(sorted(arr1), sorted(arr2, reverse=True)))
# for i in res:
#     print(i, end=" ")
