# n = int(input())
# for i in range(1, n+1):
#     for j in range(1, n):
#         j = 1
#         i = 5
#         print(j, end=' ')
#     print(i)

# N = int(input()) # Вводится натуральное число N (то есть, положительное, целое).
# nums = [] #Требуется создать двумерный (вложенный) список.
#
# for i in range(N): # Cписок размером N x N элементов.
#     nums.append([1] * N) # Cостоящий из всех единиц.
# #print(nums)
#
# # Затем, в последний столбец записать пятерки.
# for i in range(N):
#     for j in range(N):
#         nums[i][-1] = 5
# #print(nums)
# # Вывести этот список на экран в виде таблицы чисел, как показано в примере ниже.
# for r in nums:
#     for x in r:
#         if x == r[-1]:
#             print(x, end='') # В конце строк пробелов быть не должно.
#         else:
#             print(x, end=' ')
#     print()

# n = int(input())
# a = []
# for i in range(n):
#     a.append([1] * n)
# print(a)
# for i in range(n):
#     for j in range(n):
#         a[j][-1] = 5
#
# for i in a:
#     print(*i)

n = 5
a = [[0, 1, 0, 0, 1],
     [0, 0, 0, 0, 0],
     [1, 0, 0, 0, 0],
     [0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0]]
res = 'ДА'
for i in range(n):
    # for j in range(n):
    print(i + i, end=' ')



print(res)