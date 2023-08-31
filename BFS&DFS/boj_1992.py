# https://www.acmicpc.net/problem/1992

import sys
from collections import deque

def div(mat, N):
    sum_mat = sum(mat, [])

    if len(set(sum_mat)) == 1:
        return f'{max(sum_mat)}'

    div_N = N//2

    temp1 = [m[:div_N] for m in mat[:div_N]]
    temp2 = [m[div_N:] for m in mat[:div_N]]
    temp3 = [m[:div_N] for m in mat[div_N:]]
    temp4 = [m[div_N:] for m in mat[div_N:]]

    return f'({div(temp1, div_N)}{div(temp2, div_N)}{div(temp3, div_N)}{div(temp4, div_N)})'

N = int(sys.stdin.readline())
mat = list()
for _ in range(N):
    mat.append(list(map(int, list(sys.stdin.readline()[:-1]))))

# N = 8
# mat = [
#     [1,1,1,1,0,0,0,0],
#     [1,1,1,1,0,0,0,0],
#     [0,0,0,1,1,1,0,0],
#     [0,0,0,1,1,1,0,0],
#     [1,1,1,1,0,0,0,0],
#     [1,1,1,1,0,0,0,0],
#     [1,1,1,1,0,0,1,1],
#     [1,1,1,1,0,0,1,1],
# ]

print(div(mat, N))