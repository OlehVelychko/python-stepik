s1, s2 = map(str, input().split())
a = len(s2)
b = s1[1:a:2]
c = s2[1::2]
print(b == c)