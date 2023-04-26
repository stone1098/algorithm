'''
박성원이 캠프 때 쓸 N개의 랜선을 만들어야 하는데 너무 바빠서 영식이에게 도움을 청했다.

이미 오영식은 자체적으로 K개의 랜선을 가지고 있다.
그러나 K개의 랜선은 길이가 제각각이다. 
박성원은 랜선을 모두 N개의 같은 길이의 랜선으로 만들고 싶었기 때문에 K개의 랜선을 잘라서 만들어야 한다. 
예를 들어 300cm 짜리 랜선에서 140cm 짜리 랜선을 두 개 잘라내면 20cm는 버려야 한다. (이미 자른 랜선은 붙일 수 없다.)

편의를 위해 랜선을 자르거나 만들 때 손실되는 길이는 없다고 가정하며, 
기존의 K개의 랜선으로 N개의 랜선을 만들 수 없는 경우는 없다고 가정하자. 
그리고 자를 때는 항상 센티미터 단위로 정수길이만큼 자른다고 가정하자. 
N개보다 많이 만드는 것도 N개를 만드는 것에 포함된다. 
이때 만들 수 있는 최대 랜선의 길이를 구하는 프로그램을 작성하시오.

1. 이분탐색 돌리기
2. 특정 길이 length가 n을 만족해도 length보다 큰 값도 만족할 수 있으니, 조건 추가
'''
import sys

k, n = map(int, sys.stdin.readline().split())

lan_list = []

for _ in range(k):
    lan_list.append(int(sys.stdin.readline()))

l = 1
r = max(lan_list)

while l <= r:
    mid = (l + r) // 2
    
    answer = sum([lan // mid for lan in lan_list])
    
    if answer >= n:
        if sum([lan // (mid+1) for lan in lan_list]) >= n:
            l = mid + 1
        else:
            break
    else:
        r = mid

print(mid)