# lst1 = list(map(int, input().split()))
# lst2 = list()
# for i, item in enumerate(lst1):
#     item = item ** 2
#     lst2.append(item)
# print(*lst2)

# lst = list(map(int, input().split()))
# for i, value in enumerate(lst):
#     lst[i] = value ** 2
# print(*lst)

# lst = list(map(int, input().split()))
# lst2 = []
# for i, value in enumerate(lst):
#         lst2.append(value)
#         lst2.append(value)
# print(*lst2)

#    8 5 32 4

# lst = list(map(float, input().split()))
# m = lst[1]
# for i, item in enumerate(lst):
#     if item < m:
#         m = item
# print(m)

# lst = list(map(float, input().split()))
# for i, item in enumerate(lst):
#     if item < 0:
#         lst[i] = -1.0
# print(*lst)

# 10+25-12
n = input().replace(' ', '')
a = n
n = n.replace('+', '*').replace('-', '*')
s = n.split('*')
res = int(s[0])
b = 1
for i, item in enumerate(a):
    if item == '+':
        res = res + int(s[b])
        # print(res, b)
        b = b + 1

    elif item == '-':
        res = res - int(s[b])
        # print(res, b)
        b = b + 1

print(res)