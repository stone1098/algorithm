# https://school.programmers.co.kr/learn/courses/30/lessons/68645

def solution(n):    
    tri = [[0] * i for i in range(1, n+1)]

    depth = 0
    idx = 0
    last = n-1
    number = 1
    
    flag = 'D'
    
    for i in range(n, 0, -1):
        if flag == 'D':
            for j in range(i):
                tri[depth+j][idx] = number
                number += 1
            idx += 1
            depth += 2
            flag = 'R'

        elif flag == 'R':
            for j in range(i):
                tri[last][idx+j] = number
                number += 1
            last -= 1
            flag = 'U'
            
        elif flag == 'U':
            for j in range(i):
                tri[last-j][-idx] = number
                number += 1
            flag = 'D'

    return sum(tri, [])

print(solution(4)) # return [1,2,9,3,10,8,4,5,6,7]
print(solution(5)) # return [1,2,12,3,13,11,4,14,15,10,5,6,7,8,9]