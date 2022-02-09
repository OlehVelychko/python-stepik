def get_nod(a, b):
    """
    Реализуем быстрый алгоритм Эвклида для вычисления НОД двух чисел
    :param a: первое большее число
    :param b: второе меньшее число
    :return: возвращаем НОД
    """
    if a < b:
        a, b = b, a

    while b != 0:
        a, b = b, a % b

    return a


# print(get_nod(18, 24))
# help(get_nod)


def test_nod(func):
    # --- тест № 1
    a = 28
    b = 35
    res = func(a, b)
    if res == 7:
        print("тест № 1 успешный")
    else:
        print("тест № 1 провален")


test_nod(get_nod)