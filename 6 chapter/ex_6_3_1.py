# t = (3.4, -56.7)
#
# n = tuple(map(int, input().split()))
# print(t + n)


# cities = tuple(input().split())
# town = 'Москва'
#
# if town not in cities:
#     cities += (town, )
#
# print(*cities)

# t = tuple(input().split())
# t = t + ('Москва',) if 'Москва' not in t else t
# print(*t)


# cities = tuple(input().split())
# town = 'Ульяновск'
#
# if town in cities:
#     c2 = list(cities)
#     c2.remove(town)
#     cities = tuple(c2)
#
# print(*cities)


# t = tuple(input().split())
# t = tuple(v for v in t if v != 'Ульяновск')
# print(*t)


# names = tuple(input().lower().split())
#
# names = (x for x in names if 'ва' in x)
# print(*names)


# n = tuple(input().split())
#
# for i in n:
#     if 'ва' in i.lower():
#         print(i.lower(),end=' ')


# n = tuple(map(int, input().split()))
# a = n[0]
# m = [a]
# for i in n:
#     if i not in m:
#         m.append(i)
#     a = i
#
# print(*m)


# tup = tuple(input().split())
# tup2 = ()
#
# for i in tup:
#     if i not in tup2:
#         tup2 += i,
#
# print(*tup2)
#
#
# e = tuple(map(int, input().split()))
# d = dict.fromkeys(e)
# d = tuple(d.keys())
# print(*d)


# n = tuple(map(int, input().split()))
#
# for i in range(len(n)):
#     # print(i, n.count(i), n[i])
#     # print(i, n.count(n[i]), n[i])
#     if n.count(n[i]) > 1:
#         print(i, end=' ')

# print([n.index(x) for x in tup_2 if n.count(x) > 1])


# t = ((1, 0, 0, 0, 0),
#      (0, 1, 0, 0, 0),
#      (0, 0, 1, 0, 0),
#      (0, 0, 0, 1, 0),
#      (0, 0, 0, 0, 1))
# N = int(input())
# s = ''
#
# for i in t:
#     if t.index(i) < N:
#         print(*[i[j] for j in range(len(i)) if j < N])


# n = int(input())
#
# t = ((1, 0, 0, 0, 0),
#      (0, 1, 0, 0, 0),
#      (0, 0, 1, 0, 0),
#      (0, 0, 0, 1, 0),
#      (0, 0, 0, 0, 1))
#
# t1 = ()
#
# for i in range(n):
#     t1 += t[i][:n],
#
# for i in t1:
#     print(*i)


# import sys
#
# # считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))
#
# # здесь продолжайте программу (используйте список lst_in)
# menu = ()
# for i, j in enumerate(lst_in):
#     menu += tuple(j.split()),
#
# print(menu)

# t = tuple(tuple(phrase.split()) for phrase in lst_in)
#
# print(t)
