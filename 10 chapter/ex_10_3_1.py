import random
# установка "зерна" датчика случайных чисел, чтобы получались одни и те же случайные величины
random.seed(1)

# здесь продолжайте программу
# a, b = map(int, input().split())
# res = random.uniform(a, b)
# print(round(res, 2))

# a, b = map(int, input().split())
# res = random.randint(a, b)
# print(res)

lst = input().split()
res = random.choice(lst)
print(res)