# https://www.acmicpc.net/problem/1759

import sys
from itertools import combinations

answer = []

L, C = map(int, sys.stdin.readline().split())
word = list(sys.stdin.readline().rstrip().split(' '))

# 자음과 모음 나누기
g_word = [w for w in word if w in 'aeiou']
c_word = [w for w in word if w not in 'aeiou']
g_len = len(g_word)
c_len = len(c_word)

# 모음이 1개부터 L-2개까지 들어가는 경우
for i in range(1, L-2+1):
    if i <= g_len and L-i <= c_len:
        g_comb = list(combinations(g_word, i))
        c_comb = list(combinations(c_word, L-i))

        for g in g_comb:
            for c in c_comb:
                a = list()
                a = list(g) + list(c)
                a.sort()
                a = ''.join(a)
                answer.append(a)

answer.sort()
for a in answer:
    print(a)