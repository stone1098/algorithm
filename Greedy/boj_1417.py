'''
다솜이는 선거를 조작하려고 한다.
다솜이의 기계는 각 사람들이 누구를 찍을 지 미리 읽을 수 있다. 
현재 후보는 N명이다. 
다솜이는 이 기계를 이용해서 그 마을의 주민 M명의 마음을 모두 읽었다.
다솜이는 사람들의 마음을 읽어서 자신을 찍지 않으려는 사람을 돈으로 매수해서 국회의원에 당선이 되게 하려고 한다. 
마음을 읽은 결과 기호 1번이 5표, 기호 2번이 7표, 기호 3번이 7표 라고 한다면, 
2번 후보를 찍으려고 하던 사람 1명과, 3번 후보를 찍으려고 하던 사람 1명을 매수하면, 당선이 된다.
다솜이가 매수해야하는 사람의 최솟값을 출력하는 프로그램을 작성하시오.

1. max에서 하나를 빼서 1번에게 줌
2. 반복
'''
# 5, 10, 7, 3, 8 -> 4
import sys

n = int(sys.stdin.readline())
votes = []
for _ in range(n):
    votes.append(int(sys.stdin.readline()))
  
answer = 0

while votes.index(max(votes)) != 0:
    votes[votes.index(max(votes))] -= 1
    votes[0] += 1
    answer += 1

print(answer)