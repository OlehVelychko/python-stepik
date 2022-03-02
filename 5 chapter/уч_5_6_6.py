# lst_in = [[2, 3, 4, 5, 6],
#           [3, 2, 7, 8, 9],
#           [4, 7, 2, 0, 4],
#           [5, 8, 0, 2, 1],
#           [6, 9, 4, 1, 2]
#           ]
#
# flag = 'ДА'
#
# for i in range(5):
#     for j in range(5):
#         if lst_in[i][j] != lst_in[j][i]:
#             flag = 'НЕТ'
#
# print(flag)


# arr = list(map(int, input().split()))
#
# arr_2 = []
# for i in range(len(arr)):
#     arr_2.append(min(arr))
#     arr.remove(min(arr))
# print(arr_2)


nominals = [1, 2, 4, 8, 16, 32, 64]
n = int(input())
res = []

while n > 0:
    if n == max(nominals):
        res.append(max(nominals))
        break

    if n > max(nominals):
        res.append(max(nominals))
        # print(n, res)
        n = n - max(nominals)
    else:
        nominals.remove(max(nominals))

print(res)
