# https://www.acmicpc.net/problem/1012

def dfs(f, visited, group, idx):
    if f not in visited:
        # 방문한 적 없다면 visited = True후, 그룹 번호 추가
        visited.append(f)
        group.append(idx)
        x, y = f
        
        if [x+1, y] in field:
            dfs([x+1, y], visited, group, idx)
        if [x, y+1] in field:
            dfs([x, y+1], visited, group, idx)
        if [x-1, y] in field:
            dfs([x-1, y], visited, group, idx)
        if [x, y-1] in field:
            dfs([x, y-1], visited, group, idx)
        
import sys
sys.setrecursionlimit(10000)

T = int(sys.stdin.readline())
answer = []

for i in range(T):
    w, h, num = map(int, sys.stdin.readline().split())
    
    group = list()
    field = list()
    
    for i in range(num):
        x, y = map(int, sys.stdin.readline().split())
        field.append([x, y])
    
    visited = list()
    idx = 1
    
    for f in field:
        dfs(f, visited, group, idx)
        
        idx += 1 
    
    answer.append(len(set(group)))

[print(a) for a in answer]