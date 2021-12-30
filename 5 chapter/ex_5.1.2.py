# s = 0
# n = int(input())
# while n != 0:
#     s = s + n
#     n =int(input())
# print(s)

# s = input()
# while '--' in s:
#     s = s.replace('--', '-')
# print(s)

n = int(input())
p = 1
while n:
    p *= n % 10
    n //= 10
print(p)