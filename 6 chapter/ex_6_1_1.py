# items = input().split()
# a = [items[x].split('=') for x in range(len(items))]
# b = [[x[0], int(x[1])] for x in a]
# d = dict(b)
# print(*sorted(d.items()))

# d = dict(c.split('=') for c in input().split())
# for c in d:
#     d[c] = int(d[c])
# print(*sorted(d.items()))

# lst_in = input().split()
#
# lst = [[i.split('=')[0], int(i.split('=')[1])] for i in lst_in]
#
# d = dict(lst)
#
# print(*sorted(d.items()))

# x = [i.split('=') for i in input().split()]
# d = {}
# for key, value in x:
#     d[key] = int(value)
#
# print(*sorted(d.items()))
# print(x)

# lst_in = ['5=отлично', '4=хорошо', '3=удовлетворительно']
# print(lst_in)
# x = [i.split('=') for i in lst_in]
# # print(x)
# d = {}
# for key, value in x:
#     d[int(key)] = value
# print(*sorted(d.items()))

# import sys
#
# # считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))
#
# # здесь продолжайте программу (используйте список lst_in)
# lst = [i.split('=') for i in lst_in]
# d = {int(i): v for i, v in lst}
# print(*sorted(d.items()))

# import sys
#
# # считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))
#
# # здесь продолжайте программу (используйте список lst_in)
# d = {}
# for s in lst_in:
#     row = s.split('=')
#     d[int(row[0])] = row[1]
#
# print(*sorted(d.items()))

# import sys
#
# # считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# d = {}
# for i in lst_in:
#     key, value = i.split('=')
#     d[int(key)] = value
# print(*sorted(d.items()))