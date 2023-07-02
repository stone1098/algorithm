from collections import deque

def solution(n, left, right):
    arr = deque()
    
    for i in range(left, right+1):
        x, y = i%n, i//n
        num = max(x, y) + 1
        arr.append(num)
        
    return list(arr)

print(solution(3, 2, 5))
print(solution(4, 7, 14))