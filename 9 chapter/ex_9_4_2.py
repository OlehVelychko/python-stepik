# sasha = set(map(int, input().split()))
# galya = set(map(int, input().split()))
#
# dubl = sasha & galya
# # print(dubl)
#
# res = filter(lambda x: x % 2 == 0, dubl)
# print(*sorted(res))

mails = list(map(str, input().split()))
from string import ascii_letters


def validate(mail):
    for x in mail:
        if '@' in x:
            for y in x:
                if '1' in y:

                    return y
            # return all(map(lambda c: c in ascii_letters or c in '1234567890', mail))


# def filter(arr):
#     for x in arr:
#         if is

res = filter(validate, mails)
print(*res)
