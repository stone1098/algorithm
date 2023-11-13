# https://www.acmicpc.net/problem/2096

'''
N줄에 0 이상 9 이하의 숫자가 세 개씩 적혀 있다. 
내려가기 게임을 하고 있는데, 이 게임은 첫 줄에서 시작해서 마지막 줄에서 끝나게 되는 놀이이다.

먼저 처음에 적혀 있는 세 개의 숫자 중에서 하나를 골라서 시작하게 된다. 
그리고 다음 줄로 내려가는데, 다음 줄로 내려갈 때에는 다음과 같은 제약 조건이 있다. 
바로 아래의 수로 넘어가거나, 아니면 바로 아래의 수와 붙어 있는 수로만 이동할 수 있다는 것이다. 
이 제약 조건을 그림으로 나타내어 보면 다음과 같다.

[☆, -, -]  [-, ☆, -]  [-, -, ☆]
[o, o, x]  [o, o, o]  [x, o, o]

별표는 현재 위치이고, 그 아랫 줄의 파란 동그라미는 원룡이가 다음 줄로 내려갈 수 있는 위치이며, 
빨간 가위표는 원룡이가 내려갈 수 없는 위치가 된다. 숫자표가 주어져 있을 때, 얻을 수 있는 최대 점수, 
최소 점수를 구하는 프로그램을 작성하시오. 점수는 원룡이가 위치한 곳의 수의 합이다.
'''
import sys
input = sys.stdin.readline

N = int(input())
max_table = [0, 0, 0]
min_table = [0, 0, 0]
for _ in range(N):
    input_list = list(map(int, input().rstrip().split()))

    max_1 = input_list[0] + max(max_table[0], max_table[1])
    max_2 = input_list[1] + max(max_table[0], max_table[1], max_table[2])
    max_3 = input_list[2] + max(max_table[1], max_table[2])

    max_table = [max_1, max_2, max_3]

    min_1 = input_list[0] + min(min_table[0], min_table[1])
    min_2 = input_list[1] + min(min_table[0], min_table[1], min_table[2])
    min_3 = input_list[2] + min(min_table[1], min_table[2])

    min_table = [min_1, min_2, min_3]

print(max(max_table), min(min_table))