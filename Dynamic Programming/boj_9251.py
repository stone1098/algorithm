# https://www.acmicpc.net/problem/9251

'''
2차원 DP를 사용하여 해결
X 0 A C A Y K P
0 0 0 0 0 0 0 0 
C 0 0 1 1 1 1 1
A 0 1 1 2 2 2 2
P 0 1 1 2 2 2 3
C 0 1 2 2 2 2 3
A 0 1 2 3 3 3 3
K 0 1 2 3 3 4 4

특정 지점 dp[i][j]가 겹치면 대각선 위 dp[i-1][j-1]의 값에 +1을 하여 저장
겹치지 않으면 dp[i-1][j]와 dp[i][j-1]중 큰 값 저장 (이전 순열 중 큰 값을 저장)
'''

import sys

A = list(sys.stdin.readline().rstrip())
B = list(sys.stdin.readline().rstrip())

A = list('ACAYKP')
B = list('CAPCAK')
# return ACAK

column = len(A)
row = len(B)

dp = [[0] * (column+1) for _ in range(row+1)]

for i in range(1, row+1): # 행
    for j in range(1, column+1): # 열
        if B[i-1] == A[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

print(dp[row][column])

######장수정 답####
import sys
input = sys.stdin.readline

s1 = input().strip()
s2 = input().strip()
dp = [0] * 1000
# dp 각 문자별로 다른 문자열을 순회하면서
# 같은 문자면 + 1, 다른 경우 누적값이 해당 위치 dp보다 작으면 갱신
for i in range(len(s1)):
    mx = 0
    for j in range(len(s2)):
        if mx < dp[j]:
            mx = dp[j]
        elif s1[i] == s2[j]:
            dp[j] = mx + 1

print(max(dp))