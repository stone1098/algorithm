# https://www.acmicpc.net/problem/1697

import sys
from collections import deque

def BFS(N, K):
    if N > K:
        return N - K
    
    q = deque([N])
    visited = deque([100001] * 100001)
    visited[N] = 0

    while q:
        n = q.popleft()

        if n == K: return visited[n]

        if n-1 > -1 and visited[n-1] > visited[n]+1:
            visited[n-1] = visited[n]+1
            q.append(n-1)
        if n+1 < 100001 and visited[n+1] > visited[n]+1 :
            visited[n+1] = visited[n]+1
            q.append(n+1)
        if n*2 < 100001 and visited[n*2] > visited[n]+1:
            visited[n*2] = visited[n]+1
            q.append(n*2)

N, K = map(int, sys.stdin.readline().split())

print(BFS(N, K))