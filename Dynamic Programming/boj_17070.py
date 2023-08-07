# https://www.acmicpc.net/problem/17070

import sys
from collections import deque


def dfs(x, y, dir):
    global count

    if x == N-1 and y == N-1:
        count += 1
        return
    
    if x + 1 < N and y + 1 < N:
        if not mat[x+1][y+1] and not mat[x+1][y] and not mat[x][y+1]:
            dfs(x+1, y+1, 1)

    if dir == 0 or dir == 1:
        if y + 1 < N:
            if mat[x][y+1] == 0:
                dfs(x, y+1, 0)
    
    if dir == 2 or dir == 1:
        if x + 1 < N:
            if mat[x+1][y] == 0:
                dfs(x+1, y, 2)

# N = int(sys.stdin.readline())

# mat = deque()
# for _ in range(N):
#     mat.append(list(map(int, sys.stdin.readline().split())))

N = 5
mat = [
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]

count = 0

dfs(0, 1, 0)

print(count)