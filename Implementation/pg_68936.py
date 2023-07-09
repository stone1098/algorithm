# https://school.programmers.co.kr/learn/courses/30/lessons/68936

'''
8행 기준
1. 통째로 본다
2. 4x4 필터를 4칸씩 이동하면서 본다
3. 2x2 필터를 4칸씩 이동하면서 본다
남은 개수 센다

만약 발견하면??
전체 1의 개수에서 - NxN + 1
'''
import numpy as np

def solution(arr):
    # 0의 개수와 1의 개수 구하기
    zero, one = 0, 0
    for a in arr:
        zero += a.count(0)
        one += a.count(1)
        
    # 필터 사이즈
    max = len(arr)
    size = len(arr)
    arr = np.array(arr)
    
    while size >= 2:
        
        square = size*size
                
        for i in range(0, max, size):
            for j in range(0, max, size):
                temp = sum(arr[i:i+size, j:j+size].reshape(-1))
                if temp == square:
                    arr[i:i+size, j:j+size] = -1
                    one -= square - 1
                elif temp == 0:
                    arr[i:i+size, j:j+size] = -1
                    zero -= square - 1
                    
        size = size // 2
        
    return [zero, one]

print(solution([
    [1,1,0,0],
    [1,0,0,0],
    [1,0,0,1],
    [1,1,1,1]])) # return [4, 9]

print(solution([
    [1,1,1,1,1,1,1,1],
    [0,1,1,1,1,1,1,1],
    [0,0,0,0,1,1,1,1],
    [0,1,0,0,1,1,1,1],
    [0,0,0,0,0,0,1,1],
    [0,0,0,0,0,0,0,1],
    [0,0,0,0,1,0,0,1],
    [0,0,0,0,1,1,1,1]])) # return [10, 15]