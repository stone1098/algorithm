# https://www.acmicpc.net/problem/16507

'''
호근이에게 보여줄 R×C 크기의 사진이며, 각 픽셀은 밝기를 나타낸다. 
호근이가 사진의 일부분이라도 볼 수 있는지 알아보기 위해서는 
두 점 (r1, c1)과 (r2, c2)를 꼭짓점으로 하는 직사각형의 밝기 평균을 구해야 한다. 

호근이에게 보여줄 R×C 크기의 사진이 주어질 때, 사진의 일부분에 해당하는 밝기 평균을 구하여라.

첫 번째 줄에는 사진의 크기를 의미하는 정수 R, C (1 ≤ R, C ≤ 1,000)와 
사진 일부분의 밝기 평균을 알아볼 개수를 의미하는 정수 Q (1 ≤ Q ≤ 10,000)가 주어진다.

다음 R개의 줄에 걸쳐 R×C 크기의 사진 정보가 주어지며, 
사진의 각 픽셀에는 밝기를 의미하는 정수 K (1 ≤ K ≤ 1,000)가 주어진다.

다음 Q개의 각 줄에는 사진의 일부분을 나타내기 위한 두 꼭짓점을 의미하는 정수 
r1, c1, r2, c2 (1 ≤ r1 ≤ r2 ≤ R, 1 ≤ c1 ≤ c2 ≤ C)가 주어진다.

Q개의 각 줄에 주어진 사진에서 두 점 (r1, c1)과 (r2, c2)를 꼭짓점으로 하는 직사각형의 밝기 평균을 출력한다. 
평균은 정수 나눗셈으로 몫만 취한다.

1. 이미지의 입력과 동시의 누적합 테이블을 생성한다.
2. 좌표를 통해 loc[r][c2] - loc[r][c1]을 통해 해당 라인의 값을 구한다.
3. 누적 후 나눗셈 실행

(개선방안) 2차원 누적합 테이블을 사용한다.
'''

import sys, time
input = sys.stdin.readline

R, C, Q = map(int, input().split())

prefix_table = list()
prefix_table.append([0] * (C+1))
for _ in range(R):
    prefix_row = [0] * (C+1)
    row = [0]
    row.extend(list(map(int, input().split())))
    
    for i in range(1, C+1):
        prefix_row[i] = prefix_row[i-1] + row[i]

    prefix_table.append(prefix_row)

loc_list =  list()
for _ in range(Q):
    loc_list.append(list(map(int, input().split())))

for loc in loc_list:
    total = 0
    r1, c1, r2, c2 = loc

    for i in range(r1, r2+1):
        total += (prefix_table[i][c2] - prefix_table[i][c1-1])

    print(total//((r2-r1+1) * (c2-c1+1)))

# 4 3 5
# 25 93 64
# 10 29 85
# 80 63 71
# 99 58 86
# 2 2 2 3
# 3 2 3 3
# 1 2 2 2
# 1 2 4 3
# 2 3 2 3