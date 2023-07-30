# https://www.acmicpc.net/problem/12865

N, K = 4, 7
wv = [
    [0, 0],
    [6, 13],
    [4, 8],
    [3, 6],
    [5, 12],
]

# import sys

# N, K = map(int, sys.stdin.readline().split())

# wv = [[0, 0]]
# for _ in range(N):
#     w, v = map(int, sys.stdin.readline().split())
#     wv.append([w, v])

dp = [[0] * (K+1) for _ in range(N+1)] # N * K 배열 구성

for i in range(1, N+1):
    dp[i] = dp[i-1].copy()
    for j in range(1, K+1):
        if wv[i][0] <= j:
            dp[i][j] = max(dp[i-1][j], wv[i][1] + dp[i-1][j-wv[i][0]])

for e in dp:
    print(e)