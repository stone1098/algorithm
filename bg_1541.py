# https://www.acmicpc.net/problem/1541

import sys, re

s = sys.stdin.readline()
num = s.replace('-', ' ').replace('+', ' ').split(' ')
operator = list(re.sub(r'[0-9]', '', s))
answer = int(num.pop(0))

flag = 1

for i in range(len(num)):
    if operator[i] == '-':
        flag = -1
    answer += (int(num[i]) * flag)
    
print(answer)