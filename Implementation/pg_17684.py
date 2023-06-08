# https://school.programmers.co.kr/learn/courses/30/lessons/17684

def solution(msg):
    answer = []
    
    # 사전 생성
    words = [chr(65 + i) for i in range(26)]
    
    word = ''
    for m in msg:
        word += m
        
        if word not in words:
            words.append(word)
            answer.append(words.index(word[:-1]) + 1)
            word = m

    answer.append(words.index(word) + 1)
    
    return answer

print(solution('KAKAO')) # return [11, 1, 27, 15]
print(solution('TOBEORNOTTOBEORTOBEORNOT')) # return [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]