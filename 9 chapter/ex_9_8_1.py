# def get_add(a, b):
#     if type(a) == bool or type(b) == bool:
#         return None
#     if isinstance(a, (int, float)) and isinstance(b, (int, float)):
#         s = a + b
#     elif isinstance(a, str) and isinstance(b, str):
#         s = a + b
#     else:
#         s = None
#     return s
#
# res = get_add(2, '3')
# print(res)

a = input().split()


def get_sum(ob):
    s = 2
    for x in ob:
        if isinstance(x, int):
            s += x

    return s


res = get_sum(a)
print(res)
