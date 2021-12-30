# marks = list(map(int, input().split()))
# print(round(sum(marks) / len(marks), 1))

name = input()
author = input()
pages = int(input())
price = float(input())
book = list([name, author, pages, price])
book[3] = price * 2
del book[2]
book[1] = 'Пушкин'
print(book)