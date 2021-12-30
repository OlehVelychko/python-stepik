# n = int(input())
# a = 1
# b = 1
# c = a + b
# f = [a, b]
# while len(f) < n:
#     f.append(c)
#     a = b
#     b = c
#     c = a + b
# print(*f)

# 2 4 8 16  // 3 + 3 + 3 + 3 // 11
# 3 hours = 2 kletki
# n = kol_hours

# n = int(input())
# a = 2
# lst = [a]
# while len(lst) < n // 3:
#     lst.append(a ** 2)
#     lst[-1] = a ** len(lst)
# print(lst[-1])

# n = int(input())
# year = 1
# s = 1000
# while year <= n:
#     s = s * 1.05
#     year += 1
# print(round(s, 2))

# n, m = map(int, input().split())
# a = n + 1
# lst = [a]
# while lst[-1] < m:
#     a += 2
#     lst.append(a)
# print(*lst[:-1])

lst = []
a = 100
while a < 1000:
    if a % 47 == 43 and a % 3 == 0:
        lst.append(a)
    a += 1
print(*lst)