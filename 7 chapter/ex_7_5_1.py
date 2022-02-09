# def get_even(*args):
#     return [x for x in args if x % 2 == 0]
#
#
# a = list(map(int, input().split()))
# print(a)
# b = get_even(*a)
# print(*b)


# def get_biggest_city(*args):
#     res = ''
#     for x in args:
#         if len(x) > len(res):
#             res = x
#             continue
#
#     return res
#
#
# a = input().split()
# print(get_biggest_city(*a))


# def get_data_fig(*args, **kwargs):
#     res = []
#     res.append(sum(args))
#     if 'type' in kwargs:
#         res.append(kwargs.get('type'))
#     if 'color' in kwargs:
#         res.append(kwargs.get('color'))
#     if 'closed' in kwargs:
#         res.append(kwargs.get('closed'))
#     if 'width' in kwargs:
#         res.append(kwargs.get('width'))
#
#     return tuple(res)
#
#
# a = get_data_fig(3, 1, 6, type=True, color=13)
# print(a)


# def get_data_fig(*args, **kwargs):
#     kwargs = [kwargs[i] for i in ['type', 'color', 'closed', 'width'] if i in kwargs]
#     return (sum(args), *kwargs)


# def get_data_fig(*args, **kwargs):
#     res = (sum(args),)
#     for x in ['type', 'color', 'closed', 'width']:
#         if x in kwargs:
#             res += (kwargs[x],)
#     return res


