# def func_show(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         print(f"Площадь прямоугольника: {res}")
#         return res
#
#     return wrapper
#
#
# @func_show
# def get_sq(width, height):
#     res = width * height
#     return res
#
#
# # get_sq = func_show(get_sq)
# res = get_sq(5, 3)
#
#
# def func_show(func):
#     def wrapper(*args, **kwargs):
#         print(f'Площадь прямоугольника: {func(*args, **kwargs)}')
#     return wrapper
#
#
# def get_sq(width, height):
#     return width * height
#
#
# def func_show(func):
#     def show_text(*args,**kwargs):
#         res = func(*args,**kwargs)
#         print(f"Площадь прямоугольника: {res}")
#     return show_text
#
#
# def get_sq(width, height):
#     sq = width * height
#     return sq


# s_menu = input()


# def show_menu(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         start = 1
#         for x in res:
#             print(f'{start}. {x}')
#             start += 1
#
#     return wrapper
#
#
# @show_menu
# def get_menu(string):
#     array = string.split(' ')
#     return array


# res = get_menu(s_menu)
# print(res)
# res = get_menu(s_menu)


# s_digits = input()
#
#
# def sort_array(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         return sorted(res)
#
#     return wrapper
#
#
# @sort_array
# def get_array(string):
#     array = [int(x) for x in string.split()]
#     return array
#
#
# lst = get_array(s_digits)
# print(*lst)
