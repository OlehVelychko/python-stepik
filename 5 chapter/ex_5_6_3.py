# n = int(input())
# for i in range(2, n):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         print(i, end=' ')

# n = int(input())
n = 5
a = [[0, 1, 1, 0, 1],
     [0, 0, 0, 0, 0],
     [1, 0, 0, 0, 0],
     [0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0]]
res = 'ДА'
for i in range(n-1):
    for j in range(n-1):
        if a[i][j] == 1:
            if a[i][j + 1] == 1 or a[i + 1][j + 1] == 1 or a[i + 1][j] == 1:
                res = 'НЕТ'
                break

for i in range(4):
    for j in range(5):
        if a[i][4] == 1 and a[i+1][4] == 1:
            res = 'НЕТ'
            break

for i in range(5):
    for j in range(4):
        if a[4][j] == 1 and a[4][j+1] == 1:
            res = 'НЕТ'
            break

if a[3][4] == 1 and a[4][3] == 1:
    res = 'НЕТ'

print(res)

# for i in a:
# #     # if 1 in i:
# #     #     print('sfvfvs')
#     print(i)
