# a = input().split()
# b = input().split()
# s = set(set(a).intersection(set(b)))
# print(*sorted(s))


# a = set(map(int, input().split()))
# b = set(map(int, input().split()))
#
# s = set(a - b)
# print(*sorted(s))


# a = set(map(int, input().split()))
# b = set(map(int, input().split()))
#
# f = a ^ b
# print(*sorted(f))


set_1 = set(input().split()) # Получаем пользовательские данные
set_2 = set(input().split()) # Получаем пользовательские данные

c = set_2 & set_1
# print("ДА" if set_1 == set_2 else "HET")
print(c == set_1)