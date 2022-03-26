# sasha = set(map(int, input().split()))
# galya = set(map(int, input().split()))
#
# dubl = sasha & galya
# # print(dubl)
#
# res = filter(lambda x: x % 2 == 0, dubl)
# print(*sorted(res))

mails = input().split()
from string import ascii_letters

adress = ascii_letters + '1234567890 @.'


def validate_one(mail):
    for x in mail:
        if x == '@':
            for y in mail[mail.index(x) + 1::]:
                if y == '.':
                    return True


def validate_two(mail):
    mails = []
    if validate_one(mail):
        for x in mail:
            if x not in adress:
                # print(x)
                break

            mails.append(mail)

    return mails


res_3 = filter(validate_two, mails)
for i in res_3:
    print(i, end=' ')


# test = validate_two('$fg9@fd.com')
# print(test)
