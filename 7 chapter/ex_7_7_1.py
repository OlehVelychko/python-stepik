# N = int(input())


# def get_rec_N(N, value=1):
#     print(value)
#     if value < N:
#         get_rec_N(N, value+1)


# get_rec_N(N)


# def get_rec_N (n):
#     if n > 1:
#         get_rec_N(n-1)
#     print(n)


# digits = list(map(int, input().split()))
#
#
# def getsum(digits):
#     if len(digits) == 1:
#         return digits
#     else:
#         b = digits.pop()
#         digits[-1] += b
#         return getsum(digits)
#
#
# a = getsum(digits)
# print(a)


# N = int(input())
#
#
# def fib_rec(N, f=[]):
#     a, b = 1, 1
#     f = [1, 1]
#     for x in range(N-2):
#         c = a + b
#         f.append(c)
#         a = b
#         b = c
#     return f
#
#
# z = fib_rec(N)
# print(*z)


# # ввод числа N
# N = int(input())
#
#
# # здесь задается функция fib_rec (переменную N не менять!)
#
# def fib_rec(N, f=[]):
#     if len(f) < N:
#         f.append(1 if len(f) < 2 else f[-1] + f[-2])
#         fib_rec(N)
#
#         return f


# # ввод числа N
# N = int(input())
#
# def fib_rec(N, f=[1, 1]):
#     if N > 2:
#         f.append(f[-1] + f[-2])
#         fib_rec(N - 1, f)
#     return f


