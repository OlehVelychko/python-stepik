# def send_text():
#     print("It's my first function")
#
#
# send_text()


# def send_message():
#     fio = input().split()
#     print(f"Уважаемый, {fio[0]} {fio[1]}! Вы верно выполнили это задание!")
#
#
# send_message()


# def get_weight(x):
#     print(f"Предмет имеет вес: {x} кг.")
#
#
# get_weight(float(input()))


# def get_array(lst):
#     print(f"Min = {min(lst)}, max = {max(lst)}, sum = {sum(lst)}")
#
#
# get_array(list(map(int, input().split())))


# def count_p(width, height):
#     p = (width + height) * 2
#     print(f"Периметр прямоугольника, равен {p}")
#
#
# width, height = map(int, input().split())
#
# count_p(width, height)


# def get_mail(mail):
#     res = ''
#     t = {'A', 'E', 'I', 'O', 'U', 'Y', 'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T',
#          'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '_', 'a', 'e', 'i', 'o', 'u', 'y',
#          'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'
#          }
#     if "@" and '.' in mail:
#         for x in mail:
#             if x == "@" or x == '.':
#                 continue
#
#             elif x in t:
#                 res = 'ДА'
#             else:
#                 res = 'НЕТ'
#                 break
#
#     else:
#         res = 'НЕТ'
#
#     print(res)
#
#
# mail = input()
# get_mail(mail)

# 'a' <= i.lower() <= 'z' or '0' <= i <= '9' or i  in '_@.']