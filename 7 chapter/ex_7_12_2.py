# def my_decorator(tag='h1'):
#     def get_tag(fn):
#         def wrapper(*args, **kwargs):
#             return f'<{tag}>{fn(*args, **kwargs)}</{tag}>'
#
#         return wrapper
#
#     return get_tag
#
#
# @my_decorator(tag='div')
# def change(stroka):
#     return stroka.lower()
#
#
# s = input()
# res = change(s)
# print(res)
