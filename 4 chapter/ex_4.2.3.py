# m, n = map(int, input().split())
# days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# lst1 = [1, 3, 5, 7, 8, 10, 12]
# lst2 = [4, 6, 9, 11]
#
# if m == 2 and n == 28:
#     print(str(m).rjust(2, '0') + '.' + str(n-1).rjust(2, '0'), str(m+1).rjust(2, '0') + '.' + str(1).rjust(2, '0'))
# elif m in lst1:
#     if m == 8 and n == 1:
#         print(str(m-1).rjust(2, '0') + '.' + str(31).rjust(2, '0'), str(m).rjust(2, '0') + '.' + str(n+1).rjust(2, '0'))
#     elif n == 31:
#         print(str(m).rjust(2, '0') + '.' + str(n-1).rjust(2, '0'),
#               str(m+1).rjust(2, '0') + '.' + str(1).rjust(2, '0'))
#     else:
#         print(str(m).rjust(2, '0') + '.' + str(n-1).rjust(2, '0'), str(m).rjust(2, '0') + '.' + str(n+1).rjust(2, '0'))
# elif m in lst2:
#     if n == 30:
#         print(str(m).rjust(2, '0') + '.' + str(n-1).rjust(2, '0'),
#               str(m + 1).rjust(2, '0') + '.' + str(1).rjust(2, '0'))
#     else:
#         print(str(m).rjust(2, '0') + '.' + str(n-1).rjust(2, '0'), str(m).rjust(2, '0') + '.' + str(n+1).rjust(2, '0'))

m, n = map(int, input().split())
lst = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if n == 1:
    print(f'{m-1:02}.{lst[m-2]} {m:02}.{n+1:02}')
elif n == lst[m-1]:
    print(f'{m:02}.{n-1:02} {m+1:02}.01')
else:
    print(f'{m:02}.{n-1:02} {m:02}.{n+1:02}')
