t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}


# здесь продолжайте программу
def my_decorator(chars=" !?"):
    def change_chars(func):
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            for x in res:
                if x in chars:
                    res = res.replace(x, '-').replace('--', '-')

            return res

        return wrapper

    return change_chars


@my_decorator(chars="?!:;,. ")
def translate(stroka):
    s = ''
    for x in stroka.lower():
        if x in t:
            s += t.get(x)
        else:
            s += x

    return s


s = input()
result = translate(s)
print(result)
