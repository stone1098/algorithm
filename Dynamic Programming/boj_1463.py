# https://www.acmicpc.net/problem/1463

'''
정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

X가 3으로 나누어 떨어지면, 3으로 나눈다.
X가 2로 나누어 떨어지면, 2로 나눈다.
1을 뺀다.

정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 
연산을 사용하는 횟수의 최솟값을 출력하시오.
'''

import sys
input = sys.stdin.readline()

N = int(input)

dp = [0] * (10000001)
dp[2] = 1
dp[3] = 1
n = 4

for i in range(4, N+1):
    if i % 2 == 0 and i % 3 == 0:
        dp[i] = min(dp[i//2] + 1, dp[i//3] + 1)
    elif i % 3 == 0:
        dp[i] = min(dp[i-1] + 1, dp[i//3] + 1)
    elif i % 2 == 0:
        dp[i] = min(dp[i-1] + 1, dp[i//2] + 1)
    else:
        dp[i] = dp[i-1] + 1

print(dp[N])