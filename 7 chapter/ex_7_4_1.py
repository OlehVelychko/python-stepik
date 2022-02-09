# def get_rect_value(a, b, type=0):
#     if type == 0:
#         return 2 * (a + b)
#     else:
#         return a * b
#
#
# res = get_rect_value(2, 4, 5)
# print(res)


# def check_password(stroka, chars='$%!?@#'):
#     for x in stroka:
#         if x in chars and len(stroka) >= 8:
#             return True
#
#             break
#
#     return False
#
#
# res = check_password(input())
# print(res)


# def translate(stroka, sep='-'):
#     t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
#          'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
#          'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
#          'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
#     new_s = ''
#     for x in stroka.lower():
#         if x in t.keys():
#             x = t.get(x)
#             new_s += x
#         elif x == ' ':
#             new_s += sep
#         else:
#             new_s += x
#
#     return new_s
#
#
# res = input()
# print(translate(res))
# print(translate(res, '+'))


def get_tag(stroka, tag='h1', up=True):
    return f'<{tag}>'.upper() + stroka + f'</{tag}>'.upper() if up else f'<{tag}>' + stroka + f'</{tag}>'


res = input()
print(get_tag(res, 'div'))
print(get_tag(res, 'div', False))