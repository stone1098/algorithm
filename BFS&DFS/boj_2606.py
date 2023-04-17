'''
신종 바이러스인 웜 바이러스는 네트워크를 통해 전파된다. 
한 컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸리게 된다.
어느 날 1번 컴퓨터가 웜 바이러스에 걸렸다. 
컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때, 
1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성하시오.
'''

import sys

def func(graph, num, virus):
    virus[num] = True
    for g in graph:
        if num==g[0] and virus[g[1]] == False:
            func(graph, g[1], virus)
        elif num==g[1] and virus[g[0]] == False:
            func(graph, g[0], virus)

num = int(sys.stdin.readline())
edge = int(sys.stdin.readline())
graph = []
for i in range(edge):
    graph.append(list(map(int, sys.stdin.readline().split())))

virus = [False] * (num+1)

func(graph, 1, virus)
print(virus.count(True)-1)