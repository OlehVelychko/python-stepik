# s = list(map(float, set(input().split())))
# print(*sorted(s))

# words = set(input().lower().split())
# print(len(words))


# s = set(input().split())
# lst = []
# for i in s:
#     i = set(i)
#     for x in i:
#         if x in '1234567890':
#             lst.append(x)
# if len(lst) == 0:
#     print('НЕТ')
# else:
#     print(*sorted(lst))

# s = set(x for x in input() if x.isdigit())
#
# if len(s) > 0:
#     print(*sorted(s))
# else:
#     print("НЕТ")


# import sys
#
# # считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))
#
# # здесь продолжайте программу (используйте список lst_in)
# print(len(set(lst_in)))


# import sys
#
# # считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)
# a = set()
# for i in lst_in:
#     # print(i.split(':')[0])
#     a.add(i.split(':')[0])
# print(len(a))

# lst = [i.split(':')[0] for i in lst_in]
# print(len(set(lst)))


# a = set()
# while True:
#     x = input()
#     a.add(x)
#     if x == 'q':
#         break
#
# print(len(a) - 1)

s, my_set = input(), set()
while s != 'q':
  my_set.add(s)
  s = input()
print(len(my_set))