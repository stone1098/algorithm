# https://www.acmicpc.net/problem/2667

# 최대 단지 수는 N이 25일 때, (13*13) + (12*12) = 313

import sys

def DFS(i, j, estate, count):
    house[i][j] = estate
    count[estate] += 1
    
    if -1 < i-1 and house[i-1][j] == 1:
        DFS(i-1, j, estate, count)
    if i+1 < size and house[i+1][j] == 1:
        DFS(i+1, j, estate, count)
    if -1 < j-1 and house[i][j-1] == 1:
        DFS(i, j-1, estate, count)
    if j+1 < size and house[i][j+1] == 1:
        DFS(i, j+1, estate, count)

size = int(sys.stdin.readline())
house = list()
for _ in range(size):
    house.append(list(map(int, list(sys.stdin.readline()[:-1]))))

# size = 7
# house = [
#     [0,1,1,0,1,0,0],
#     [0,1,1,0,1,0,1],
#     [1,1,1,0,1,0,1],
#     [0,0,0,0,1,1,1],
#     [0,1,0,0,0,0,0],
#     [0,1,1,1,1,1,0],
#     [0,1,1,1,0,0,0],
# ]

estate = 2
count = [0] * 320

for i in range(size):
    for j in range(size):
        if house[i][j] == 1:
            DFS(i, j, estate, count)
            estate += 1

print(estate-2)

count.sort()
count = [c for c in count if c != 0]
for c in count:
    print(c)