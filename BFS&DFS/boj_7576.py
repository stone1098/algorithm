# https://www.acmicpc.net/problem/7576

import sys
from collections import deque

def bfs(m, n, house):

    delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    q = deque()
    for i in range(n):
        for j in range(m):
            if house[i][j] == 1:
                q.append((i, j))

    while q:
        i, j = q.popleft()
        day = house[i][j] + 1

        for d in delta:
            dx = i + d[0]
            dy = j + d[1]
            if dx < n and dx > -1 and dy < m and dy > -1:
                if house[dx][dy] == 0:
                    house[dx][dy] = day
                    q.append((dx, dy))

    l = sum(house, [])

    return max(l)-1 if l.count(0) == 0 else -1

m, n = map(int, sys.stdin.readline().split())

house = deque()
for _ in range(n):
    house.append(list(map(int, sys.stdin.readline().split())))

# m, n = 6, 4

# house = deque([
#     [0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 1],
# ])

answer = bfs(m, n, house)
print(answer)