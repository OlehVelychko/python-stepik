# p = [0] * 10
# while p.count(1) < 5:
#     n = int(input())
#     if p[n] == 1:
#         continue
#
#     p[n] = 1
#
# print(*p)

# n = 1
# p = 1
# while n:
#     n = int(input())
#     if n == 0:
#         continue
#
#     elif n > 0:
#         p *= n
#
# print(p)

res, x = 1, 1
while x:
    x = int(input())
    if x <= 0:
        continue
    res *= x
print(res)