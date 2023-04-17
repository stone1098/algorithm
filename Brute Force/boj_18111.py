'''
고르지 않은 땅에는 집을 지을 수 없기 때문에 땅의 높이를 모두 동일하게 만드는 ‘땅 고르기’ 작업을 해야 한다.
lvalue는 세로 N, 가로 M 크기의 집터를 골랐다. 
집터 맨 왼쪽 위의 좌표는 (0, 0)이다.
우리의 목적은 이 집터 내의 땅의 높이를 일정하게 바꾸는 것이다. 
우리는 다음과 같은 두 종류의 작업을 할 수 있다.

    1. 좌표 (i, j)의 가장 위에 있는 블록을 제거하여 인벤토리에 넣는다.
    2. 인벤토리에서 블록 하나를 꺼내어 좌표 (i, j)의 가장 위에 있는 블록 위에 놓는다.

1번 작업은 2초가 걸리며, 2번 작업은 1초가 걸린다.

‘땅 고르기’ 작업에 걸리는 최소 시간과 그 경우 땅의 높이를 출력하시오.
답이 여러 개 있다면 그중에서 땅의 높이가 가장 높은 것을 출력하시오.

단, 집터 아래에 동굴 등 빈 공간은 존재하지 않으며, 집터 바깥에서 블록을 가져올 수 없다. 
또한, 작업을 시작할 때 인벤토리에는 B개의 블록이 들어 있다. 땅의 높이는 256블록을 초과할 수 없으며, 음수가 될 수 없다.

1. 블록 제거 조건 -> 바닥의 수가 1이상
2. 블록 추가 조건 -> 바닥의 수가 256이하, 인벤토리가 1이상
'''

'''
브루트포스를 이용한 접근 방법
1. 0 ~ 256까지 각 블록 높이를 맞춘 시간을 계산 후, 가장 빠른 값 return
'''
import sys

n, m, b = map(int, sys.stdin.readline().split())

field = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

answer, height = sys.maxsize, -1

for h in range(257):
    add_block, sub_block = 0, 0
    for i in range(n):
        for j in range(m):
            # i보다 낮은 블록
            if field[i][j] < h: 
                add_block += (h - field[i][j])
            # i보다 높은 블록
            else:
                sub_block += (field[i][j] - h)
            
    if (b + sub_block) >= add_block:
        if answer >= (add_block + (sub_block*2)):
            answer = add_block + (sub_block*2)
            height = h
    
print(answer, height)