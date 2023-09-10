# https://www.acmicpc.net/problem/5430

import sys
from collections import deque

def func(word, n, arr):
    if n == 0:
        arr = deque()
    else:
        arr = deque(list(map(int, arr[1:-1].split(','))))

    flag = 1

    for w in word:
        if w == 'R':
            if flag:
                flag = 0
            else:
                flag = 1
        else:
            if len(arr) == 0:
                return 'error'
            arr.popleft() if flag else arr.pop()

    if flag == 1:
        return str(list(arr)).replace(' ', '')
    else:
        arr.reverse()
        return str(list(arr)).replace(' ', '')

T = int(sys.stdin.readline())
answer = list()

for _ in range(T):
    word = sys.stdin.readline().strip()
    n = int(sys.stdin.readline())
    arr = sys.stdin.readline().strip()

    answer.append(func(word, n, arr))

for a in answer:
    print(a)