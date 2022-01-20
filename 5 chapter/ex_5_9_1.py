# matrix = [[1, 2, 3, 4],
#           [5, 6, 7, 8],
#           [9, 8, 7, 6],
#           [5, 4, 3, 2]]
#
# lst = [x
#        for row in matrix
#        for x in row]
# print(*lst[::-1])

import sys

# считывание списка из входного потока
s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]

lst = [x
       for row in lst_in
       for x in row]
print(*lst[::-1])