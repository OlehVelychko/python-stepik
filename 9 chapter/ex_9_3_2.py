# t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
#      'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
#      'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
#      'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}

# здесь продолжайте программу
# def translate(stroka):
#     s = ''
#     for x in stroka.lower():
#         if x in t:
#             s += t.get(x)
#         elif x in "1234567890?!:;,. ":
#             s += '-'
#         else:
#             s += x
#
#     return s
#
#
# s = input()
#
# gen = map(translate, s)
# # for i in gen:
# #     print(i, end='')
# print(''.join(gen))


# print(*map(lambda x: t.get(x, '-'), input().lower()), sep='')


cities = input().split()

ar = list(map(lambda x: x if len(x) > 5 else '-', cities))
print(*ar)
