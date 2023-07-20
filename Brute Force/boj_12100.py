# https://www.acmicpc.net/problem/12100

from collections import deque
import sys

def action(N, matrix, direction):
    temp = []
    if direction == 'L':
        for line in matrix:
            # 한 줄에 대하여 0을 모두 제거
            line = [l for l in line if l != 0]
            for i in range(1, len(line)):
                if line[i-1] == line[i]:
                    line[i-1] *= 2
                    line[i] = 0
            # 다시 0을 제거
            line = [l for l in line if l != 0]
            # 부족한 0 채워줌
            padding = [0] * (N - len(line))
            line = line + padding
            temp.append(line)
    if direction == 'R':
        for line in matrix:
            # 한 줄에 대하여 0을 모두 제거
            line = [l for l in line if l != 0]
            for i in range(len(line)-1, 0, -1):
                if line[i] == line[i-1]:
                    line[i] *= 2
                    line[i-1] = 0
            # 다시 0을 제거
            line = [l for l in line if l != 0]
            # 부족한 0 채워줌
            padding = [0] * (N - len(line))
            line = padding + line
            temp.append(line)
    if direction == 'U':
        temp = [[0] * N for _ in range(N)]
        for j in range(N): # j번 열만 뽑아서 처리
            temp_col = list()
            for i in range(N):
                temp_col.append(matrix[i][j])
            temp_col = [t for t in temp_col if t != 0]
            for i in range(1, len(temp_col)):
                if temp_col[i] == temp_col[i-1]:
                    temp_col[i-1] *= 2
                    temp_col[i] = 0
            temp_col = [t for t in temp_col if t != 0]
            padding = [0] * (N - len(temp_col))
            temp_col = temp_col + padding
            for i in range(N):
                temp[i][j] = temp_col[i]
    if direction == 'D':
        temp = [[0] * N for _ in range(N)]
        for j in range(N): # j번 열만 뽑아서 처리
            temp_col = list()
            for i in range(N):
                temp_col.append(matrix[i][j])
            temp_col = [t for t in temp_col if t != 0]
            for i in range(len(temp_col)-1, 0, -1):
                if temp_col[i] == temp_col[i-1]:
                    temp_col[i] *= 2
                    temp_col[i-1] = 0
            temp_col = [t for t in temp_col if t != 0]
            padding = [0] * (N - len(temp_col))
            temp_col = padding + temp_col
            for i in range(N):
                temp[i][j] = temp_col[i]

    return temp

def solution(N, answer_list, move_count, matrix):
    if move_count >= 5:
        answer_list.append(max(map(max, matrix)))
        return 0
    # 첫번째 움직임
    move_count += 1
    solution(N, answer_list, move_count, action(N, matrix, 'L'))
    solution(N, answer_list, move_count, action(N, matrix, 'R'))
    solution(N, answer_list, move_count, action(N, matrix, 'U'))
    solution(N, answer_list, move_count, action(N, matrix, 'D'))

N = int(sys.stdin.readline())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))
answer_list = list()
matrix = deque(matrix)

solution(N, answer_list, 0, matrix)
print(max(answer_list))