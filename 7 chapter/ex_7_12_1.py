# def df_dec(start=5):
#     def decorate(func):
#         def wrapper(*args, **kwargs):
#             res = func(*args, **kwargs) + start
#             return res
#
#         return wrapper
#
#     return decorate
#
#
# @df_dec()
# def change(stroka):
#     res = [int(x) for x in stroka.split()]
#
#     return sum(res)
#
#
# s = input()
# df = change(s)
# print(df)


# from functools import wraps


# def decor(start=0):
#     def decorator(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             res = sum(func(*args, **kwargs)) + start
#             return res
#
#         return wrapper
#
#     return decorator
#
#
# @decor(start=5)
# def str_to_list(st):
#     'Функция преобразующая строку в список целых чисел'
#     return list(map(int, st.split()))
#
#
# s = input()
# print(str_to_list(s))


# def my_decorator(start):
#     def sum_list(fn):
#         def wropper(*args):
#             return start + fn(*args)
#
#         return wropper
#
#     return sum_list
#
#
# @my_decorator(start=5)
# def get_list(s):
#     return sum(list(map(int, s.split())))
#
#
# s = input()
# summ = get_list(s)
# print(summ)

