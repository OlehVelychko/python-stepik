# a, b, c = map(int, input().split())
# if a < b and a < c:
#     print(a)
# elif b < a and b < c:
#     print(b)
# elif c < a and c < b:
#     print(c)

# w = float(input())
# if w <= 60:
#     print('1')
# elif 60 < w <= 64:
#     print('2')
# elif 64 < w <= 69:
#     print('3')
# else:
#     print('4')

# day = int(input())
# week = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
# if day == 1:
#     print(week[0])
# elif day == 2:
#     print(week[1])
# elif day == 3:
#     print(week[2])
# elif day == 4:
#     print(week[3])
# elif day == 5:
#     print(week[4])
# elif day == 6:
#     print(week[5])
# else:
#     print(week[6])

month = int(input())
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
lst1 = [1, 3, 5, 7, 8, 10, 12]
lst2 = [2]
lst3 = [4, 6, 9, 11]
if month in lst1:
    print(days[month-1])
elif month in lst2:
    print(days[month-1])
elif month in lst3:
    print(days[month - 1])