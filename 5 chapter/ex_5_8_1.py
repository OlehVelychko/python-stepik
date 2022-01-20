# n = map(float, input().split())
# lst = [float(abs(x)) for x in n]
# print(lst)

# lst = [abs(float(d)) for d in input().split()]
# print(lst)

# num = input()
# lst = [abs(float(n)) for n in num.split()]
# print(lst)

# n = input().split()
# lst = [n[x] for x in range(len(n)) if x % 2 == 0]
# print(*lst)

# print(*[float(i) for i in input().split()][::2])

lst = [float(x) for i, x in enumerate(input().split()) if i % 2 == 0]
print(*lst)