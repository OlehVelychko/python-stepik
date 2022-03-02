# from functools import wraps
#
#
# def my_decorator(fn):
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         res = fn(*args, **kwargs)
#         return sum(res)
#
#     return wrapper
#
#
# @my_decorator
# def get_list(stroka):
#     """Функция для формирования списка целых значений"""
#     res = [int(x) for x in stroka.split()]
#
#     return res
#
#
# s = input()
# result = get_list(s)
# print(result)
# print(get_list.__doc__)
# print(get_list.__name__)


# from functools import wraps
#
#
# # здесь продолжайте программу
# def decoratos_sum(func):
#     @wraps(func)
#     def wrapper(*args):
#         return sum(func(*args))
#
#     return wrapper
#
#
# @decoratos_sum
# def get_list(s):
#     '''Функция для формирования списка целых значений'''
#     return list(map(int, s.split()))



