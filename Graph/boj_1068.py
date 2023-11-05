# https://www.acmicpc.net/problem/1068

'''
트리에서 리프 노드란, 자식의 개수가 0인 노드를 말한다.

트리가 주어졌을 때, 노드 하나를 지울 것이다. 그 때, 남은 트리에서 리프 노드의 개수를 구하는 프로그램을 작성하시오. 
노드를 지우면 그 노드와 노드의 모든 자손이 트리에서 제거된다.

첫째 줄에 트리의 노드의 개수 N이 주어진다. N은 50보다 작거나 같은 자연수이다. 
둘째 줄에는 0번 노드부터 N-1번 노드까지, 각 노드의 부모가 주어진다. 
만약 부모가 없다면 (루트) -1이 주어진다. 셋째 줄에는 지울 노드의 번호가 주어진다.

첫째 줄에 입력으로 주어진 트리에서 입력으로 주어진 노드를 지웠을 때, 리프 노드의 개수를 출력한다.
'''

from collections import deque
import sys
input = sys.stdin.readline

def solution(tree, del_node):

    leaf = 0
    root = tree.index(-1)
    d = deque([root])

    if len(tree) == 0 or root == del_node:
        return 0
    
    # 트리 자르기
    del_list = [del_node]
    tree[del_node] = -1
    for i in range(len(tree)):
        if tree[i] in del_list:
            tree[i] = -1
            del_list.append(i)

    # 간선 생성
    edge = [[] for _ in range(50)]
    for i in range(len(tree)):
        if tree[i] != -1:
            edge[tree[i]].append(i)

    while d:
        node = d.popleft()
        if len(edge[node])==0:
            leaf += 1
        else:
            d.extend(edge[node])

    return leaf

N = int(input())
tree = list(map(int, input().rstrip().split()))
del_node = int(input())

# return 2
# N = 5
# tree = [-1, 0, 0, 1, 1]
# del_node = 0

# return 2
# N = 9
# tree = [-1, 0, 0, 2, 2, 4, 4, 6, 6]
# del_node = 4

print(solution(tree, del_node))