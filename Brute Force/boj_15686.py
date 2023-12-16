# https://www.acmicpc.net/problem/15686

'''
한 치킨집과 모든 집과의 거리를 구하는 것이 아님.
임의로 m개를 뽑은 후, 최소의 치킨 거리를 구해야 함
'''

import sys
from itertools import combinations
input = sys.stdin.readline

# 치킨 거리 계산 함수
def chickenDistance(house, alive):
    dist = 0
    for h in house:
        temp = sys.maxsize
        for a in alive:
            temp = min(temp, abs(h[0] - a[0]) + abs(h[1] - a[1]))
        dist += temp
    return dist

N, M = map(int, input().split())
city = list()
for _ in range(N):
    city.append(list(map(int, input().split())))

# N, M = 5, 2
# city = [
#     [0, 2, 0, 1, 0],
#     [1, 0, 1, 0, 0],
#     [0, 0, 0, 0, 0],
#     [2, 0, 0, 1, 1],
#     [2, 2, 0, 1, 2],
# ]

# 치킨집과 집의 좌표 저장
chicken, house = list(), list()
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            house.append((i, j))
        elif city[i][j] == 2:
            chicken.append((i, j))

comb = list(combinations(chicken, M))

answer = sys.maxsize
for c in comb:
    answer =  min(answer, chickenDistance(house, c))

print(answer)