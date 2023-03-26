'''
신종 바이러스인 웜 바이러스는 네트워크를 통해 전파된다. 
한 컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸리게 된다.
어느 날 1번 컴퓨터가 웜 바이러스에 걸렸다. 
컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때, 
1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성하시오.
'''

import sys

num = int(sys.stdin.readline())
edge = int(sys.stdin.readline())
graph = [[] for _ in range(num+1)]
for i in range(edge):
    a, b = map(int, sys.stdin.readline().split())
    print(a, b)
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (num+1)

def func(graph, num, visited):
    visited[num] = True
    for g in graph[num]:
        if visited[g] == False:
            func(graph, g, visited)
            
func(graph, 1, visited)
print(visited.count(True)-1)

print(graph)