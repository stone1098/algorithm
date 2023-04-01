'''
0 또는 양의 정수가 주어졌을 때, 
정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.

예를 들어, 주어진 정수가 [6, 10, 2]라면 
[6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.

0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 
순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.

1. permutation을 사용하면 시간초과 발생
2. (x[0], x[-1])을 기준으로 정렬했지만 시간초과 발생
3. n[i]+n[i+1]과 n[i+1]+n[i]을 비교했지만 또 시간초과 발생 (버블소트)
'''

def solution(numbers): 
    return str(int("".join(sorted(list(map(str, numbers)), key=lambda x: (x*3), reverse=True))))

print(solution([3, 30, 34, 5, 9]))