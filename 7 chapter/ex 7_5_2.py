[[1, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 0, 0]]


# def is_isolate(lst):
#     if sum(lst) == 1:
#         return True
#     else:
#         return False
#
#
# def verify(args):
#     lst_in = args
#     N = int(len(lst_in[1]))
#
#     lst_in.insert(0, [0] * N)
#     lst_in.insert(N + 1, [0] * N)
#
#     for i, v in enumerate(lst_in):
#         v.insert(0, 0)
#         v.insert(N + 1, 0)
#
#     r = []
#     s = 0
#     for row in range(1, len(lst_in) - 1):
#         for col in range(1, len(lst_in[row]) - 1):
#             if lst_in[row][col] == 1:
#                 r.append(lst_in[row - 1][col - 1])
#                 r.append(lst_in[row - 1][col])
#                 r.append(lst_in[row - 1][col + 1])
#                 r.append(lst_in[row][col - 1])
#                 r.append(lst_in[row][col + 1])
#                 r.append(lst_in[row][col])
#                 r.append(lst_in[row + 1][col + 1])
#                 r.append(lst_in[row + 1][col])
#                 r.append(lst_in[row + 1][col - 1])
#                 if is_isolate(r):
#                     s += 0
#                 else:
#                     s += 1
#                 r = []
#
#     return True if s == 0 else False


# def is_isolate(*tple):
#     return tple.count(1) <= 1
#
#
# def verify(inpt):
#     for i in range(len(inpt) - 1):
#         for j in range(len(inpt[i]) - 1):
#             if not is_isolate(inpt[i][j], inpt[i][j+1], inpt[i+1][j], inpt[i+1][j+1]):
#                 return False
#     return True


