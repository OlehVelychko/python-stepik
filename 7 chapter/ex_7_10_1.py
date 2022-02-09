# k = int(input())
#
#
# def counter_add(start=k):
#     def step():
#         nonlocal start
#         start += 5
#         return start
#
#     return step
#
#
# cnt = counter_add(k)
# print(cnt())
# print(cnt())
# print(cnt())


# k = int(input())
#
#
# def counter_add(n):
#     def up(k):
#         return k + n
#
#     return up
#
#
# cnt = counter_add(2)
# print(cnt(k))


# word = input()
#
#
# def get_tag():
#     def add(s):
#         s = '<h1>' + s + '</h1>'
#         return s
#
#     return add
#
#
# res = get_tag()
# print(res(word))


# # put your python code here
# def lock_in_tag(tag):
#     def add_str(string):
#         return f'<{tag}>{string}</{tag}>'
#     return add_str
#
#
# s = input()
# f = lock_in_tag('h1')
# print(f(s))


# # put your python code here
# def add_tag(tag="h1"):
#     def stroka(s):
#         print(f"<{tag}>{s}</{tag}>")
#
#     return stroka
#
#
# n = input()
# inp = add_tag()
# inp(n)


# def get_tag(tag):
#     def add_tag(s):
#         s = f'<{tag}>{s}</{tag}>'
#         return s
#
#     return add_tag
#
#
# t = input()
# word = input()
#
# res = get_tag(t)
# print(res(word))


def set_col(tp):
    def change(digits):
        if tp == 'list':
            digits = list(digits)
        else:
            digits = tuple(digits)
        return digits

    return change


t = input()
arr = map(int, input().split())

res = set_col(t)
lst = res(arr)
print(lst)