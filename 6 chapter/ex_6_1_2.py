# d = {}
# b = [x.split('=') for x in input().split()]
# for key, value in b:
#     d[key] = value
# if 'house' in d and 'True' in d and '5' in d:
#     print("ДА")
# else:
#     print("НЕТ")

# d = dict([i.split('=') for i in input().split()])
# print('ДА' if 'house' in d and 'True' in d and '5' in d else 'НЕТ')

d = dict([i.split("=") for i in input().split()])
check_values = ['house', 'True', '5']

for i in check_values:
    if i not in d:
        print('НЕТ')
        break
else:
    print('ДА')
