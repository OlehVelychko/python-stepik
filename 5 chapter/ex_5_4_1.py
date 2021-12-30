# n = input()
# a = -1
# for i in range(len(n) - 1):
#     if 'ра' not in n:
#         print(a)
#         break
#
#     elif (n[i] + n[i+1]) == 'ра':
#         print(i, end=' ')
#
# +7(123)456-78-99 ///  0 2 6 10 13
# phone = input()
# res = 'ДА'
# if len(phone) == 16 and phone[0] == '+' and phone[1] == '7' and phone[2] == '(' and phone[6] == ')' and phone[10] == '-' and phone[13] == '-':
#     for i in phone:
#         if i.isalpha() or i not in '123456789+-()':
#             res = 'НЕТ'
#             break
#
# else:
#     res = 'НЕТ'
# print(res)

s = '+7(xxx)xxx-xx-xx'
num = input()
count = 0
if len(s) == len(num):
    for i, item in enumerate(num):
        if s[i] == item or s[i] == 'x' and item.isdigit():
            count += 1

print('ДА' if count == 16 else 'НЕТ')

