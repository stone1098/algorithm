# https://www.acmicpc.net/problem/1149

import sys

N = int(sys.stdin.readline())

costs = []

costs.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, N):
    temp = list(map(int, sys.stdin.readline().split()))
    R = temp[0] + min(costs[i-1][1], costs[i-1][2])
    G = temp[1] + min(costs[i-1][0], costs[i-1][2])
    B = temp[2] + min(costs[i-1][0], costs[i-1][1])
    costs.append([R, G, B])
    
print(min(costs[-1]))