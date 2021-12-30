# import sys
#
# # считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# i = 0
# a = []
# while len(lst_in) > i:
#     if not lst_in[i].count(' '):
#         a.append(lst_in[i])
#     i += 1
#
# print(*a)

lst = list(map(int, input().split()))
i = 0
c = 0
while len(lst) > i:
    if lst[i] % 2 != 0:
        c = c + 1
    i += 1
print(c)