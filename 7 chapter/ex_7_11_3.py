# t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
#      'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
#      'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
#      'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
#
# # здесь продолжайте программу
# s = input().lower()
#
#
# def get_def(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         for x in res:
#             res = res.replace('--', '-')
#         return res
#
#     return wrapper
#
#
# @get_def
# def translate(string):
#     s1 = ''
#     for x in string:
#         if x in t:
#             s1 += t.get(x)
#         elif x in ": ;.,_":
#             x = '-'
#             s1 += x
#         else:
#             s1 += x
#
#     return s1
#
#
# a = translate(s)
# print(a)
