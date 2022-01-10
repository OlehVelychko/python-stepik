# n = int(input())
# for i in range(2, n):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         print(i, end=' ')

# n = int(input())
n = 5
a = [[0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 1, 0, 0],
     [0, 0, 0, 0, 1]]
res = 'ДА'


def isTouchOne(array, i, j):
    if array[i][j] == 1:
        if j + 1 < len(array) - 1 and array[i][j + 1] == 1:
            return True
        if i + 1 < len(array) - 1 and array[i + 1][j] == 1:
            return True
        if i + 1 < len(array) - 1 and j + 1 < len(array) - 1 and array[i + 1][j + 1] == 1:
            return True
        if i + 1 <= n - 1 and j - 1 >= 0 and array[i + 1][j - 1] == 1:
            return True
    return False

isTouch = False
for i in range(n):
    for j in range(n):
        isTouch = isTouchOne(a, i, j)
        if isTouch:
            res = "НЕТ"
            break
        else:
            res = "ДА"
    if isTouch:
        break

print(res)
