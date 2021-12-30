# for x in range(10, -1, -1):
#     print(x, end=' ')

# print(*range(-10, 0, 2))

# print(*range(1, 20, 3))

# a = map(int, input().split())
# a = list(a)
# s = 0
# for x in a:
#     if x % 2 != 0:
#         s += x
# print(s)

# cities = list(map(str, input().split()))
#
# # cities = list(cities)
# for i in range(len(cities)):
#     cities[i] = len(cities[i])
# print(*cities)

# n = int(input())
# for i in range(1, n+1):
#     if n % i == 0:
#         print(i)

# res = 'ДА'
# n = int(input())
# for i in range(2, n):
#     if n % i == 0:
#         res = 'НЕТ'
#         break
#
#     i += 1
#
# print(res)

# res = ''
# cities = list(map(str, input().lower().split()))
# ex = ['ь', 'ъ', 'ы']
# for i in range(len(cities) - 1):
#     if cities[i][-1] in ex:
#         if cities[i][-2] == cities[i+1][0]:
#             res = 'ДА'
#         else:
#             res = 'НЕТ'
#             break
#
#     elif cities[i][-1] == cities[i+1][0]:
#         res = 'ДА'
#     else:
#         res = 'НЕТ'
#         break
#
# print(res)

lst = [city.rstrip("ьъы") for city in input().split()]
for i in range(1,len(lst)):
    if lst[i-1][-1] != lst[i][0].lower():
        print("НЕТ")
        break
else:
    print("ДА")