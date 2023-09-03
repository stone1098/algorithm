# https://www.acmicpc.net/problem/9465

'''
특정 지점 dp[0][i]에서 이전 dp[1][i-1]을 선택하거나, 이전 값을 포기하는 dp[0][i-1] - s[0][i-1]을 선택
'''

import sys

def detech(N, sticker):
    dp = [[0] * N for _ in range(2)]
    dp[0][0], dp[1][0] = sticker[0][0], sticker[1][0]

    for i in range(1, N):
        dp_0 = max(dp[1][i-1], dp[0][i-1] - sticker[0][i-1]) + sticker[0][i]
        dp_1 = max(dp[0][i-1], dp[1][i-1] - sticker[1][i-1]) + sticker[1][i]
        dp[0][i], dp[1][i] = dp_0, dp_1
    
    return max(dp[0][-1], dp[1][-1])

answer = list()
T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    sticker = list()
    for _ in range(2):
        sticker.append(list(map(int, sys.stdin.readline().split())))

    answer.append(detech(N, sticker))

# N = 7
# sticker = [
#     [10, 30, 10, 50, 100, 20, 40],
#     [20, 40, 30, 50, 60, 20, 80],
# ]

for a in answer:
    print(a)