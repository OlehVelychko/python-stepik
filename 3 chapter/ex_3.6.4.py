# lst = list(map(int, input().split()))
# lst = sorted(lst, reverse=True)
# print(*lst)

lst = list(input().split())
cities = ["Москва", "Тверь", "Вологда"]
lst = cities + lst
print(*lst)