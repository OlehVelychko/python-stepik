# fio = list(input().split())
# print(fio[2], fio[0][0] + '.' + fio[1][0] + '.')

# s = list(map(int, input().split()))
# s.sort()
# print(*s[:3])

lst = list(map(int, input().split()))
lst.append(lst.pop() % 2 != 0)
print(*lst)