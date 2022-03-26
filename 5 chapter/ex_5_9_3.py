# import math
#
# n = list(map(int, input().split()))
# # n = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# # n = [1, 2, 3, 4]
#
#
# flag = int(math.sqrt(len(n)))
# res = [[n[x] for x in range(i, i+flag)] for i in range(0, len(n), flag)]
# print(res)


# t = ["– Скажи-ка, дядя, ведь не даром",
#      "Я Python выучил с каналом",
#      "Балакирев что раздавал?",
#      "Ведь были ж заданья боевые,",
#      "Да, говорят, еще какие!",
#      "Недаром помнит вся Россия",
#      "Как мы рубили их тогда!"
#      ]
#
# lst = [[x for x in i.split() if len(x) > 3] for i in t]
# print(lst)


# lst_in = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9],
#           [5, 4, 3]]
#
# A = [[x[i] for x in lst_in] for i in range(len(lst_in[0]))]
# for row in A:
#     print(*row)
