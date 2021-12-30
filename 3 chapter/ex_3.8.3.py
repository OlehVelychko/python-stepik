# a = list(map(int, input().split()))
# print(a.count(2))

rivers = list(input().split())
rivers.sort()
rivers.pop(0)
print(*rivers)
