# https://www.acmicpc.net/problem/1932

'''
tri_sum[i].append( max(tri[i-1][j] + tri[i][j], tri[i-1][j] + tri[i+1][j]) )
'''

# n = 5

# tri = [
#     [7],
#     [3, 8],
#     [8, 1, 0],
#     [2, 7, 4, 4],
#     [4, 5, 2, 6, 5],
# ]

import sys

n = int(sys.stdin.readline())
tri = list()
for _ in range(n):
    tri.append(list(map(int, sys.stdin.readline().split())))

sum_tri = list()
for i in range(1, n+1):
    sum_tri.append([0] * i)

sum_tri[0] = tri[0]

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            sum_tri[i][j] = sum_tri[i-1][j] + tri[i][j]
        elif j == i:
            sum_tri[i][j] = sum_tri[i-1][j-1] + tri[i][j]
        else:
            sum_tri[i][j] = max(sum_tri[i-1][j] + tri[i][j], sum_tri[i-1][j-1] + tri[i][j])

print(max(sum_tri[-1]))