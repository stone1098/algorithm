# https://www.acmicpc.net/problem/14891

'''
첫째 줄에 1번 톱니바퀴의 상태, 둘째 줄에 2번 톱니바퀴의 상태, 
셋째 줄에 3번 톱니바퀴의 상태, 넷째 줄에 4번 톱니바퀴의 상태가 주어진다. 
상태는 8개의 정수로 이루어져 있고, 12시방향부터 시계방향 순서대로 주어진다. N극은 0, S극은 1로 나타나있다.

다섯째 줄에는 회전 횟수 K(1 ≤ K ≤ 100)가 주어진다. 다음 K개 줄에는 회전시킨 방법이 순서대로 주어진다. 
각 방법은 두 개의 정수로 이루어져 있고, 첫 번째 정수는 회전시킨 톱니바퀴의 번호, 두 번째 정수는 방향이다. 
방향이 1인 경우는 시계 방향이고, -1인 경우는 반시계 방향이다.

2번, 6번 index를 사용
시계 : 7번 pop -> 0번으로 input
반시계 : 0번 pop -> 맨 뒤로 append
'''

import sys
from collections import deque
input = sys.stdin.readline

w = deque()
w.append(deque([0,0,0,0,0,0,0,0]))
for _ in range(4):
    w.append(deque(list(map(int, list(input().rstrip())))))

k = int(input())
act = list()
for _ in range(k):
    wn, dir = map(int, input().split())
    act.append((wn, dir))

# w = deque([
#     deque([0,0,0,0,0,0,0,0]),
#     deque([1,0,1,0,1,1,1,1]),
#     deque([0,1,1,1,1,1,0,1]),
#     deque([1,1,0,0,1,1,1,0]),
#     deque([0,0,0,0,0,0,1,0])
# ])
# k = 2
# act = [(3, -1), (1, 1)] # return 7

for a in act:
    wn, dir = a[0], a[1]
    q = deque([(wn, dir)])
    
    # 뒷쪽 방향
    for i in range(wn, 1, -1):
        if w[i][6] != w[i-1][2]:
            dir *= -1
            q.append((i-1, dir))
        else:
            break
    
    # 앞쪽 방향
    dir = a[1]
    for i in range(wn, 4):
        if w[i][2] != w[i+1][6]:
            dir *= -1
            q.append((i+1, dir))
        else:
            break

    while q:
        wn, dir = q.popleft()
        
        # 시계방향
        if dir == 1:
            temp = w[wn].pop()
            w[wn].appendleft(temp)
        else:
            temp = w[wn].popleft()
            w[wn].append(temp)

print(w[1][0] * 1 + w[2][0] * 2 + w[3][0] * 4 + w[4][0] * 8)