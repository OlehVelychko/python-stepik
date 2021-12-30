# s = input()
# print(s.replace(" ", "\\"))

s = input()
a = s.replace(" ", "\"")
s = a.replace("\"", "\'", 1)
print(s)