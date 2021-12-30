# a = float(input())
# b = float(input())
# d = a if a > b else b
# print(d)

# a = int(input())
# res = 'кратно 3' if a % 3 == 0 else 'не кратно 3'
# print(res)

# s = input().lower()
# res = 'палиндром' if s == s[::-1] else 'не палиндром'
# print(res)

# a = int(input())
# msg = 'True' if a == 1 else 'False'
# print(msg)

# t = int(input())
# next = t + 1 if t != 59 else 0
# print(next)

# m = ['#до', 'ре', 'ми', '#фа', 'соль', 'ля', 'си']
# a, b, c = map(int, input().split())
# res = m[a-1] + ' ' + m[b-1] + ' ' + m[c-1]
# print(res)

m = ['', 'до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']
a, b, c = map(int, input().split())
print('#' + m[a] if m[a] == 'до' or m[a] == 'фа' else m[a],
      '#' + m[b] if m[b] == 'до' or m[b] == 'фа' else m[b],
      '#' + m[c] if m[c] == 'до' or m[c] == 'фа' else m[c])