# array = input().split()
# lst = []
# for x in range(4):
#     lst.append(array[x])
# print(*lst)


# *lst, x, y, z = input().split()
# print(*lst)


# cities = input().split()
# lst_c = *cities,
# print(lst_c)


# a, b = map(int, input().split())
# c = a, b+1,
# lst = list(range(*c))
# print(*lst)


# digits = list(map(float, input().split()))
# cities = input().split()
# lst = *digits, *cities,
# print(*lst)


import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))


menu = {'Главная': 'home', 'Архив': 'archive', 'Новости': 'news'}
# здесь продолжайте программу (используйте список lst_in и menu)
lst = dict((s.split('=')[0], s.split('=')[1]) for s in lst_in)

menu = {**menu, **lst}


print(*menu)
print(*menu.values())
