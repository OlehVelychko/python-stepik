stroka_1 = input()
stroka_2 = input()


# def get_array(a, b):
#     for x in a:
#         res1 = a.split(' ')
#     for x in b:
#         res2 = b.split(' ')
#
#     return res1, res2


def set_dec(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        d = dict()
        for x in res:
            d = dict.fromkeys(x)
        return d

    return wrapper


@set_dec
def get_array(a, b):
    for x in a:
        res1 = a.split(' ')
    for x in b:
        res2 = b.split(' ')

    return res1, res2


# @set_dec
# def get_array(*args):
#     for x in args:
#         res = x.split(' ')
#         return res


result = get_array(stroka_1, stroka_2)
print(result)
