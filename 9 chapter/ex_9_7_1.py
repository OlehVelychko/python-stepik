# arr = input().split()
# res = sorted(arr, key=len, reverse=True)
# print(*res)

# arr = input().split()
# por = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']
#
# res = sorted(arr, key=lambda x: por.index(x))
# print(*res)


zvan = ['рядовой', 'сержант', 'старшина', 'прапорщик', 'лейтенант', 'капитан', 'майор', 'подполковник', 'полковник']
import sys

# считывание списка из входного потока (переменную lst_in не менять)
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список строк lst_in)
lst = [x.split('=') for x in lst_in]
print(lst)
res = sorted(lst, key=lambda x: zvan.index(x), reverse=True)
print(res)