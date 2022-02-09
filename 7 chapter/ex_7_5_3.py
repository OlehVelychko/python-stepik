def str_min(*args):
    if args[0] < args[1]:
        return args[0]
    else:
        return args[1]


res = str_min('ритА', 'рита')
print(res)


def str_min3(*args):
    f = str_min(args[0], args[1])
    return str_min(f, args[2])


res2 = str_min3('РИта', 'ритА', 'рита')
print(res2)


def str_min4(*args):
    f = str_min3(args[0], args[1], args[2])
    return str_min(f, args[3])
