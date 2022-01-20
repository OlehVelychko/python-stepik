# d = dict([[x[:2], x[2:]] for x in input().split()])
# print(*sorted(d.items()))

# a = input().split()
# d = dict()
# for i in range(len(a)):
#     b = a[i][0:2]
#     c = a[i]
#     d.setdefault(b, [])
#     d[b].append(c)
# print(*sorted(d.items()))

d = dict()
for i in input().split():
    d.setdefault(i[0:2], []).append(i)
print(*sorted(d.items()))
