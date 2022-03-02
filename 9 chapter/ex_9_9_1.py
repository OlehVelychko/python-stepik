# # put your python code here
# a = map(float, input().split())
# res = any(map(lambda x: x < 0, a))
# print(res)


def is_string(lst):
    return all(isinstance(x, str) for x in lst)


