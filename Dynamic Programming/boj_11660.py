# https://www.acmicpc.net/problem/11660

# import sys

# N, M = map(int, sys.stdin.readline().split())

# mat = list()
# for _ in range(N):
#     mat.append(list(map(int, sys.stdin.readline().split())))

# xy_list = list()
# for _ in range(M):
#     xy_list.append(list(map(int, sys.stdin.readline().split())))

N, M = 4, 3
mat = [
    [1, 2, 3 ,4],
    [2, 3, 4 ,5],
    [3, 4, 5, 6],
    [4, 5, 6, 7],
]
xy_list = [
    [2, 2, 3, 4],
    [3, 4, 3, 4],
    [1, 1, 4, 4],
]

sum_mat = [[0] * (N+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, N+1):
        sum_mat[i][j] = mat[i-1][j-1] + sum_mat[i-1][j] + sum_mat[i][j-1] - sum_mat[i-1][j-1]

for xy in xy_list:
    x1, y1, x2, y2 = xy[0], xy[1], xy[2], xy[3]
    s = sum_mat[x2][y2] - sum_mat[x2][y1-1] - sum_mat[x1-1][y2] + sum_mat[x1-1][y1-1]
    print(s)