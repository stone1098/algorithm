'''
세준이는 크기가 N×N인 배열 A를 만들었다. 배열에 들어있는 수 A[i][j] = i×j 이다.
이 수를 일차원 배열 B에 넣으면 B의 크기는 N×N이 된다. B를 오름차순 정렬했을 때, B[k]를 구해보자.
배열 A와 B의 인덱스는 1부터 시작한다.

핵심 1. b[k]의 의미는 b[k] 보다 작거나 같은 원소가 k개 이상 있다는 의미
핵심 2. b[k]보다 작은 원소의 수를 구하는 방법은 i/b[k]
핵심 3. b[k]는 k보다 무조건 작거나 같다
'''

n = int(input())
k = int(input())

L, R = 1, k
answer = 0

while L<=R:
    cnt = 0
    mid = (L + R) // 2
    
    for i in range(1, n+1):
        cnt += min(mid//i, n)
    
    if cnt >= k:
        answer = mid
        R = mid - 1
    elif cnt < k:
        L = mid + 1
        
print(answer)