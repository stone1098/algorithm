# https://www.acmicpc.net/problem/2133

'''
N = 2일 때, d[2] = 3
N = 4일 때, d[N-2] * d[2] + d[N-N] * 2
N, d[N-2] * 3 + d[N-4] * 2 + ... + d[N-N] * 2
'''

import sys

dp = [0] * 31
dp[0] = 1
dp[2] = 3

N = int(sys.stdin.readline())

for i in range(4, N+1, 2):
    dp[i] = dp[i-2] * 3
    for j in range(4, i+1, 2):
        dp[i] += dp[i-j] * 2

print(dp[N])