# https://www.acmicpc.net/problem/1261

'''
알고스팟 운영진이 모두 미로에 갇혔다. 미로는 N*M 크기이며, 총 1*1크기의 방으로 이루어져 있다. 
미로는 빈 방 또는 벽으로 이루어져 있고, 빈 방은 자유롭게 다닐 수 있지만, 벽은 부수지 않으면 이동할 수 없다.

알고스팟 운영진은 여러명이지만, 항상 모두 같은 방에 있어야 한다. 즉, 여러 명이 다른 방에 있을 수는 없다. 
어떤 방에서 이동할 수 있는 방은 상하좌우로 인접한 빈 방이다. 즉, 현재 운영진이 (x, y)에 있을 때, 
이동할 수 있는 방은 (x+1, y), (x, y+1), (x-1, y), (x, y-1) 이다. 단, 미로의 밖으로 이동 할 수는 없다.

벽은 평소에는 이동할 수 없지만, 알고스팟의 무기 AOJ를 이용해 벽을 부수어 버릴 수 있다. 벽을 부수면, 빈 방과 동일한 방으로 변한다.

만약 이 문제가 알고스팟에 있다면, 운영진들은 궁극의 무기 sudo를 이용해 벽을 한 번에 다 없애버릴 수 있지만, 
안타깝게도 이 문제는 Baekjoon Online Judge에 수록되어 있기 때문에, sudo를 사용할 수 없다.

현재 (1, 1)에 있는 알고스팟 운영진이 (N, M)으로 이동하려면 벽을 최소 몇 개 부수어야 하는지 구하는 프로그램을 작성하시오.

첫째 줄에 미로의 크기를 나타내는 가로 크기 M, 세로 크기 N (1 ≤ N, M ≤ 100)이 주어진다.
다음 N개의 줄에는 미로의 상태를 나타내는 숫자 0과 1이 주어진다. 0은 빈 방을 의미하고, 1은 벽을 의미한다.
(1, 1)과 (N, M)은 항상 뚫려있다.

1. 좌표는 (1, 1), wall은 0으로 시작
2. heapq를 사용하는데, 정렬 기준은 wall
3. 각 네 방향으로 범위 내에 있으면 힙큐에 추가하며, (n, m) 도달 시 종료
'''
import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

def solution(row, column, rooms):

    wall = 0
    q = list()
    heapq.heappush(q, (wall, 0, 0))

    visited = [[INF] * column for _ in range(row)]

    while q:
        wall, r, c = heapq.heappop(q)
        visited[r][c] = wall

        if r == row-1 and c == column-1:
            return wall

        if r+1 < row:
            if rooms[r+1][c] == 0 and visited[r+1][c] > wall:
                heapq.heappush(q, (wall, r+1, c))
            elif visited[r+1][c] > wall+1:
                heapq.heappush(q, (wall+1, r+1, c))
        if c+1 < column:
            if rooms[r][c+1] == 0 and visited[r][c+1] > wall:
                heapq.heappush(q, (wall, r, c+1))
            elif visited[r][c+1] > wall+1:
                heapq.heappush(q, (wall+1, r, c+1))
        if r-1 >= 0:
            if rooms[r-1][c] == 0 and visited[r-1][c] > wall:
                heapq.heappush(q, (wall, r-1, c))
            elif visited[r-1][c] > wall+1:
                heapq.heappush(q, (wall+1, r-1, c))
        if c-1 >= 0:
            if rooms[r][c-1] == 0 and visited[r][c-1] > wall:
                heapq.heappush(q, (wall, r, c-1))
            elif visited[r][c-1] > wall+1:
                heapq.heappush(q, (wall+1, r, c-1))
    
    return -1

column, row = map(int, input().split())
rooms = list()
for _ in range(column):
    rooms.append(list(map(int, list(input().rstrip()))))

# rooms = [
#     [0,0,1,1,1,1],
#     [0,1,0,0,0,0],
#     [0,0,1,1,1,1],
#     [1,1,0,0,0,1],
#     [0,1,1,0,1,0],
#     [1,0,0,0,1,0],
# ]
# row, column = 6, 6

print(solution(row, column, rooms))