# lst = list(map(int, input().split()))
# d = dict.fromkeys(lst)
# for i in d:
#     a = []
#     print(i, end=' ')

# print(*dict.fromkeys(input().split()))

num = input().split()
d = dict.fromkeys(num)
lst = d.keys()
print(*lst)