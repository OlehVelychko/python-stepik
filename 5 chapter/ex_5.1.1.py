# n, m = map(int, input().split())
# while n <= m:
#     res = n ** 2
#     n += 1
#     print(res, end=' ')
#
# c = float(input())
# i = 2
# while i <= 10:
#     sum = i * c
#     i += 1
#     print(round(sum, 1), end=' ')

n = int(input())
i = 1
sum = 0
while i <= n:
    sum = sum + 1 / i
    i += 1
print(round(sum, 3))