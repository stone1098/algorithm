# https://school.programmers.co.kr/learn/courses/30/lessons/76502

def check(s):
    while True:
        if '()' not in s and '[]' not in s and '{}' not in s:
            break
        s = s.replace('()', '')
        s = s.replace('[]', '')
        s = s.replace('{}', '')
    return 1 if len(s) == 0 else 0

def solution(s):
    answer = 0
    
    for i in range(len(s)):
        answer += check(s)
        s = s[1:] + s[0]
    
    return answer

print(solution("[](){}")) # return 3
print(solution("}]()[{")) # return 2
print(solution("[)(]")) # return 0
