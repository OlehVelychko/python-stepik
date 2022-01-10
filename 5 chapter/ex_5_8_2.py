# lst = [int(x) for x in input()]
# print(lst)

n = int(input())
mtrx = [[0] * n for x in range(n)]
print(mtrx)
#

for i in range(n):
    mtrx[i][i] = 1
print(mtrx)

for row in mtrx:
    print(*row)
    # print(' '.join([str(elem) for elem in row]))

# n = int(input())
#
# lst = [[1 if i == j else 0 for i in range(n)] for j in range(n)]
#
# for i in lst:
#     print(*i)