# s = list(input().lower())
# print(s)
# if 't' in s and 'h' in s and 'o' in s:
#     print('ДА')
# else:
#     print('НЕТ')

# cities = list(map(str, input().split()))
# if 'Москва' in cities:
#     cities.remove('Москва')
# print(*cities)

a, b, c, d = map(int, input().split())
if max(a, b) >= (max(c, d) + 2) and min(a, b) >= (min(c, d) + 2):
    print('ДА')
else:
    print('НЕТ')