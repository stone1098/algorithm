# https://www.acmicpc.net/problem/12851
# https://www.acmicpc.net/board/view/38887#comment-69010

'''
수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 
동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다. 
만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 
순간이동을 하는 경우에는 0초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 
수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

1. 힙큐를 통한 다익스트라로 문제 해결
2. 첫번째 제출의 실패 이유 = 힙큐의 정렬 기준을 cost가 아닌 loc로 정함
3. loc 기준 정렬 시, 18->17이 아닌 16->17이 먼저 도달하기 때문에 실패
'''

import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

def BFS(n, k):
    if n >= k:
        return n-k
    
    dp = [INF] * 200002
    cost = 0
    if n <= 0:
        dp[n] =0
        n, cost = 1, 1

    queue = []
    heapq.heappush(queue, [cost, n])

    while queue:
        cost, loc = heapq.heappop(queue)
        if loc == k:
            return cost
        elif loc <= 0 and loc >= 100001:
            continue

        if dp[loc*2] > cost and loc*2 <= 100000:
            dp[loc*2] = cost
            heapq.heappush(queue, [cost, loc*2])
        if dp[loc+1] > cost+1 and loc+1 <= 100000:
            dp[loc+1] = cost+1
            heapq.heappush(queue, [cost+1, loc+1])
        if dp[loc-1] > cost+1 and loc-1 >= 0:
            dp[loc-1] = cost+1
            heapq.heappush(queue, [cost+1, loc-1])

    return -1

n, k = map(int, input().split())

print(BFS(n, k))