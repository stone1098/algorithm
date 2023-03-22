'''
N개의 회의에 대하여 회의실 사용표를 만들려고 한다. 
각 회의 I에 대해 시작시간과 끝나는 시간이 주어져 있고, 
각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수를 찾아보자. 
한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다.
회의의 시작시간과 끝나는 시간이 같을 수도 있다. 이 경우에는 시작하자마자 끝나는 것으로 생각하면 된다.
'''

'''
1. 종료 시간을 기준으로 정렬하되, 종료 시간이 같으면 시작 시간을 기준으로 정렬
2. 그 후 종료 시간이 다음 회의의 시작 시간보다 작거나 같으면 회의 추가
'''

import sys

n = int(sys.stdin.readline())
meetings = []

for i in range(n):
    meetings.append(list(map(int, sys.stdin.readline().split())))

meetings = sorted(meetings, key=lambda x : (x[1], x[0]))
result = 0
end = 0

for m in meetings:
    if m[0] >= end:
        result += 1
        end = m[1]

print(result)