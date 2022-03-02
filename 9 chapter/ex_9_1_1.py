# gen = (x for x in range(2, 10001))

# # ввод значений a и b (переменные a и b не менять!)
# a, b = map(int, input().split())
#
# # здесь продолжайте программу
# gen = (x**2 for x in range(a, b+1))
# tp = tuple(gen)
# print(tp)


# # ввод значений a и b (переменные a и b не менять!)
# a, b = map(int, input().split())
#
# # здесь продолжайте программу
# gen = (abs(x) for x in range(a, b))
# lst = list(gen)
# for i in range(len(lst)):
#     print(lst[i])
#     if i > 3:
#         break


# a, b = map(int, input().split())
# gen = (abs(x) for x in range(a, b + 1))
# for i in range(5):
#     print(next(gen))


# a = int(input())
# gen = (abs(x) for x in range(-a, a + 1))
# gen_kub = (x**3 for x in gen)
# for i in range(4):
#     print(next(gen_kub), end=' ')


# from string import ascii_lowercase
# gen = (ascii_lowercase[x] + y for x in range(2) for y in ascii_lowercase)
# for i in range(51):
#     print(next(gen), end=' ')


# from string import ascii_lowercase
#
# gen = (i + j for i in ascii_lowercase for j in ascii_lowercase)
#
# for x in range(50):
#     print(next(gen), end=" ")