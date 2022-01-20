# +71234567890 Сергей +71234567810 Сергей +51234567890 Михаил +72134567890 Николай

# import sys
#
# # считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))
#
# # здесь продолжайте программу (используйте список lst_in)
# d = dict()
# for i in range(len(lst_in)):
#     a = lst_in[i].split()
#     # print(a[1])
#     b = a[1]
#     c = a[0]
#     d.setdefault(b, [])
#     d[b].append(c)
# print(*sorted(d.items()))

import sys
lst_in = list(map(str.strip, sys.stdin.readlines()))
d = dict()
for i in lst_in:
    i = i.split()
    d.setdefault(i[1], []).append(i[0])
print(*sorted(d.items()))