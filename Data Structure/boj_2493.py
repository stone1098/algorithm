# https://www.acmicpc.net/problem/2493

'''
1. 첫 번째 요소를 스택에 추가, N-2부터 idx 시작

2. 스택의 top보다 작으면 stack에 추가

2-1 스택의 top보다 크면, pop후 answer[pop_idx]에 idx+1 입력
2-1-1 스택의 top보다 작아지거나 스택이 비면, 스택에 현재 idx 추가

3 idx가 0 도달 후에도 스택이 차있으면 answer[pop_idx]에 0입력
'''

import sys
from collections import deque

N = int(sys.stdin.readline())
tower = list(map(int, sys.stdin.readline().split()))
# N = 5
# tower = [6, 9, 5, 7, 4]
answer = [0] * N

first_idx = N-1
first_n = tower[N-1]

stack = deque([(first_idx, first_n)])
idx = N-2

while idx >= 0:

    # 스택의 top의 값보다 작으면, 스택에 추가
    if stack[-1][1] > tower[idx]:
        stack.append((idx, tower[idx]))
    # 스택의 top보다 크면, top가 tower[idx]보다 클 때까지 pop()
    else:
        while len(stack) != 0 and stack[-1][1] < tower[idx]:
            pop_idx, pop_n = stack.pop()
            answer[pop_idx] = idx + 1
        stack.append((idx, tower[idx]))
    idx -= 1

if len(stack) != 0:
    while stack:
        pop_idx, pop_n = stack.pop()
        answer[pop_idx] = 0

for a in answer:
    print(a, end=' ')