# https://www.acmicpc.net/problem/7569

'''
창고에 보관되는 토마토들 중에는 잘 익은 것도 있지만, 아직 익지 않은 토마토들도 있을 수 있다. 
보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다. 
하나의 토마토에 인접한 곳은 위, 아래, 왼쪽, 오른쪽, 앞, 뒤 여섯 방향에 있는 토마토를 의미한다. 
대각선 방향에 있는 토마토들에게는 영향을 주지 못하며, 토마토가 혼자 저절로 익는 경우는 없다고 가정한다. 
철수는 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지 그 최소 일수를 알고 싶어 한다.

토마토를 창고에 보관하는 격자모양의 상자들의 크기와 익은 토마토들과 익지 않은 토마토들의 정보가 주어졌을 때,
며칠이 지나면 토마토들이 모두 익는지, 그 최소 일수를 구하는 프로그램을 작성하라. 단, 상자의 일부 칸에는 토마토가 들어있지 않을 수도 있다.

첫 줄에는 상자의 크기를 나타내는 두 정수 M,N과 쌓아올려지는 상자의 수를 나타내는 H가 주어진다. 
M은 상자의 가로 칸의 수, N은 상자의 세로 칸의 수를 나타낸다. 단, 2 ≤ M ≤ 100, 2 ≤ N ≤ 100, 1 ≤ H ≤ 100 이다. 
둘째 줄부터는 가장 밑의 상자부터 가장 위의 상자까지에 저장된 토마토들의 정보가 주어진다. 
즉, 둘째 줄부터 N개의 줄에는 하나의 상자에 담긴 토마토의 정보가 주어진다. 
각 줄에는 상자 가로줄에 들어있는 토마토들의 상태가 M개의 정수로 주어진다. 
정수 1은 익은 토마토, 정수 0 은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다. 
이러한 N개의 줄이 H번 반복하여 주어진다.

토마토가 하나 이상 있는 경우만 입력으로 주어진다.

여러분은 토마토가 모두 익을 때까지 최소 며칠이 걸리는지를 계산해서 출력해야 한다. 
만약, 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력해야 하고, 토마토가 모두 익지는 못하는 상황이면 -1을 출력해야 한다.
'''

import sys
from collections import deque
input = sys.stdin.readline

def BFS(tmt):

    q = deque([])

    for h in range(H):
        for i in range(N):
            for j in range(M):
                if tmt[h][i][j] == 1:
                    q.append((h, i, j))

    delta = [
        (-1, 0, 0),
        (1, 0, 0),
        (0, -1, 0),
        (0, 1, 0),
        (0, 0, -1),
        (0, 0, 1),
    ]

    while q:
        h, i, j = q.popleft()
        day = tmt[h][i][j]+1

        for d in delta:
            dh = h + d[0]
            dx = i + d[1]
            dy = j + d[2]

            if (0 <= dh < H) and (0 <= dx < N) and (0 <= dy < M) and tmt[dh][dx][dy] == 0:
                tmt[dh][dx][dy] = day
                q.append((dh, dx, dy))

    max = 1
    for h in range(H):
        for i in range(N):
            for j in range(M):
                if max < tmt[h][i][j]:
                    max = tmt[h][i][j]
                elif tmt[h][i][j] == 0:
                    return -1
    return max-1

M, N, H = map(int, input().rstrip().split())

tmt = list()
for _ in range(H):
    floor = list()
    for _ in range(N):
        floor.append(list(map(int, input().rstrip().split())))
    tmt.append(floor)

print(BFS(tmt))

# 1. 수동적인 if문을 쓰는 것보다 delta를 지정하여 forloop를 돌리는 것이 더 효과적임 (오타도 줄일 수 있다)
# 2. sum(list, [])보다 3중 forloop를 돌리는 것이 더 효과적임