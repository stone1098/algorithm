'''
j는 활을 쏜 횟수
1. a[i] < n-j (r[10]에선 그냥 n-j를 다 입력) 면 r[i]에 횟수 입력
2. 비교 -> 양수고, 이전 차이보다 크면 answer에 입력, 음수면 -1
'''
def compare(apeach, ryan):
    a_score = 0
    r_score = 0
    for i in range(11):
        if apeach[i] == 0 and ryan[i] == 0:
            pass
        elif apeach[i] >= ryan[i]:
            a_score += 10 - i
        else:
            r_score += 10 - i
    return r_score - a_score
    
def solution(n, info):
    answer = [-1]
    
    for i in range(10):
        ryan = [0] * 11
        diff = 0
        count = n
    
        for j in range(i, 10):
            if count >= info[j]:
                ryan[j] = info[j] + 1
                count -= info[j] + 1
            if count <= 0:
                break
        ryan[10] = count
        
        print(ryan)
    
    # return answer

print(solution(5, [2,1,1,1,0,0,0,0,0,0,0])) # [0,2,2,0,1,0,0,0,0,0,0]