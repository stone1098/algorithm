# https://www.acmicpc.net/problem/1717

'''
초기에 n+1개의 집합 {0},{1},{2},...,{n}이 있다. 
여기에 합집합 연산과, 두 원소가 같은 집합에 포함되어 있는지를 확인하는 연산을 수행하려고 한다.
집합을 표현하는 프로그램을 작성하시오.

첫째 줄에 n, m이 주어진다. m은 입력으로 주어지는 연산의 개수이다. 다음 m개의 줄에는 각각의 연산이 주어진다. 합집합은 
0 a b의 형태로 입력이 주어진다. 이는 a가 포함되어 있는 집합과, b가 포함되어 있는 집합을 합친다는 의미이다. 
두 원소가 같은 집합에 포함되어 있는지를 확인하는 연산은 1 a b의 형태로 입력이 주어진다. 
이는 a와 b가 같은 집합에 포함되어 있는지를 확인하는 연산이다.

1로 시작하는 입력에 대해서 a와 b가 같은 집합에 포함되어 있으면 
"YES" 또는 "yes"를, 그렇지 않다면 "NO" 또는 "no"를 한 줄에 하나씩 출력한다.
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n, m = map(int, input().split())
set_list = [i for i in range(n+1)]

# 경로압축 : 부모를 찾아가는 과정에서 각 노드의 부모를 직접 업데이트합니다. 즉, 3 -> 2 -> 1와 같은 연결을 3 -> 1 <- 2로 바꾸어 검색 효율을 높인다.
def findNode(x):   
    y = set_list[x]
    if y != set_list[y]:
        return findNode(y)
    else:
        return y

for _ in range(m):
    code, a, b = map(int, input().split())

    if code==0:
        a = findNode(a)
        b = findNode(b)
        if a > b:
            set_list[b] = a
        else:
            set_list[a] = b

    elif code==1:
        if findNode(a) == findNode(b):
            print("YES")
        else:
            print("NO")