# https://www.acmicpc.net/problem/2294

'''
n가지 종류의 동전이 있다.
이 동전들을 적당히 사용해서, 그 가치의 합이 k원이 되도록 하고 싶다. 
그러면서 동전의 개수가 최소가 되도록 하려고 한다. 각각의 동전은 몇 개라도 사용할 수 있다.

사용한 동전의 구성이 같은데, 순서만 다른 것은 같은 경우이다.

첫째 줄에 사용한 동전의 최소 개수를 출력한다. 불가능한 경우에는 -1을 출력한다.

첫째 줄에 n, k가 주어진다. (1 ≤ n ≤ 100, 1 ≤ k ≤ 10,000) 
다음 n개의 줄에는 각각의 동전의 가치가 주어진다. 
동전의 가치는 100,000보다 작거나 같은 자연수이다. 
가치가 같은 동전이 여러 번 주어질 수도 있다.

'''

import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
arr = set()
for _ in range(n):
    arr.add(int(sys.stdin.readline()))
arr = list(arr)
arr.sort()

# n, k = 3, 15
# arr = [1, 5, 12]
# # return 3

d = deque([(0, 0)])
dp = [-1] * (k+1)

# price는 가격, count는 동전 수
while d:
    price, count = d.popleft()

    # price가 목표값과 같으면 stop
    if price == k:
        break

    # 기존 가격에 +a를 하여 dp에 저장, 해당 가격 dp에 추가
    for a in arr:
        if price+a <= k and dp[price+a] == -1:
            dp[price+a] = count+1
            d.append((price+a, count+1))

print(dp[k])