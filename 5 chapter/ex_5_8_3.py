# cities = input()
# a = [city for city in cities.split()
#      if len(city) > 5
#      ]
# print(*a)

# n = int(input())
# lst = [x for x in range(1, n+1) if n % x == 0]
# print(*lst)

# n = int(input())
# mtrx = [[0] * n for x in range(n)]
# print(mtrx)
#
# for i in range(1, n):
#     for j in range(n):
#         mtrx[i][j] = i
# print(mtrx)
#
# for row in mtrx:
#     print(*row)

n = int(input())

lst = [[i] * n for i in range(n)]

for i in lst:
    print(*i)