# https://www.acmicpc.net/problem/1107

'''
수빈이는 채널을 돌리려고 했지만, 버튼을 너무 세게 누르는 바람에, 일부 숫자 버튼이 고장났다.

리모컨에는 버튼이 0부터 9까지 숫자, +와 -가 있다. 
+를 누르면 현재 보고있는 채널에서 +1된 채널로 이동하고, 
-를 누르면 -1된 채널로 이동한다. 
채널 0에서 -를 누른 경우에는 채널이 변하지 않고, 채널은 무한대 만큼 있다.

수빈이가 지금 이동하려고 하는 채널은 N이다. 
어떤 버튼이 고장났는지 주어졌을 때, 채널 N으로 이동하기 위해서 버튼을 최소 몇 번 눌러야하는지 구하는 프로그램을 작성하시오.
수빈이가 지금 보고 있는 채널은 100번이다.

pypy로
'''

import sys
input = sys.stdin.readline

def dfs(N, button, new_ch):
    global ch
    global diff

    # 숫자가 7자리를 넘으면 종료
    if len(new_ch) <= 6:
        new_diff = len(new_ch) + abs(N - int(new_ch))
        
        if new_diff < diff:
            ch = int(new_ch)
            diff = new_diff
        
        for b in button:
            dfs(N, button, new_ch + b)

button = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
N = int(input())
M = int(input())
if M != 0:
    rm = list(input().rstrip().split(' '))
    for r in rm:
        button.remove(r)

ch = 100
diff = abs(N-ch)

if diff > 1:
    for b in button:
        dfs(N, button, b)

print(diff)