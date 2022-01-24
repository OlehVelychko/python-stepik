# def get_not_even(x):
#     return x % 2
#
#
# m = list(map(int, input().split()))
# lst = [x for x in m if get_not_even(x)]
#
# print(*lst)


# tp = input()
#
# if tp == 'RECT':
#     def get_sq(a, b):
#         return a * b
# else:
#     def get_sq(a):
#         return a * a


# def get_length(x):
#     return len(x) >= 6


# cities = input().split()
# lst = [i for i in cities if get_length(i)]
# print(*lst)


# def get_again(x):
#     return (x, len(x))
#
#
# cities = input().split()
# d = {get_again(i)[0]: get_again(i)[1] for i in cities}
# # print(d)
# a = sorted(d, key=lambda x: d[x])
# print(*a)


def get_product(x, y):
    return x * y


numbers = list(map(int, input().split()))
print(get_product(max(numbers), min(numbers)))