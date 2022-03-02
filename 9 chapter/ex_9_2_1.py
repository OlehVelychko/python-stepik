# def get_sum(digit):
#     res = 0
#     for x in range(1, digit + 1):
#         res += x
#         yield res
#
#
# N = int(input())
# summa = get_sum(N)
# for x in summa:
#     print(x)


# 1 1 1 3 5 9 17

# def get_bal(digit):
#     a, b, c = 1, 1, 1
#     print(a, b, c, end=' ')
#     for x in range(4, digit + 1):
#         res = a + b + c
#         yield res
#         a = b
#         b = c
#         c = res
#
#
# N = int(input())
# result = get_bal(N)
# for x in result:
#     print(x, end=' ')


# import random
# from string import ascii_lowercase, ascii_uppercase
#
# # установка зерна датчика случайных чисел (не менять)
# random.seed(1)
#
#
# # здесь продолжайте программу
# def set_pas(digit):
#     chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
#     res = ''
#     for x in range(digit):
#         indx = random.randint(0, len(chars))
#         res += chars[indx]
#
#     yield res
#
#
# N = int(input())
#
# # for i in range(5):
# #     print(*set_pas(N))
#
# for i in range(5):
#     print(next(set_pas(N)))


# import random
# from string import ascii_lowercase, ascii_uppercase
#
# # установка зерна датчика случайных чисел (не менять)
# random.seed(1)
#
#
# # здесь продолжайте программу
# def set_mail(digit):
#     chars = ascii_lowercase + ascii_uppercase
#     res = ''
#     domen = '@mail.ru'
#     for x in range(digit):
#         indx = random.randint(0, len(chars))
#         res += chars[indx]
#
#     yield res + domen
#
#
# N = int(input())
#
# for i in range(5):
#     print(next(set_mail(N)))


# def get_simple():
#     digit = 100
#     ar = []
#     for x in range(2, digit + 1):
#         for y in range(2, x):
#             if x % y == 0:
#                 break
#         else:
#             ar.append(x)
#
#     return ar
#
#
# f = get_simple()
#
# for i in range(len(f)):
#     if i < 20:
#         print(f[i], end=' ')


def prime_numbers():
    i = 1
    while True:
        i += 1
        for j in range(2, 1 + i // 2):
            if i % j == 0:
                break
        else:
            yield i


gen = prime_numbers()
print(*(next(gen) for j in range(20)))