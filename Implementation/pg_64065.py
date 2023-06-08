# https://school.programmers.co.kr/learn/courses/30/lessons/64065

def solution(s):
    answer = []
    
    s = s[1:-1]
    elements = []
    
    while s.find('{') != -1:
        f_index = s.find('{') + 1
        b_index = s.find('}')
        
        temp = s[f_index:b_index].split(',')
        elements.append(temp)
        
        if b_index+2 >= len(s):
            break
        s = s[b_index+2:]
    
    elements.sort(key=lambda x : len(x))
    
    for element in elements:
        for e in element:
            if e not in answer:
                answer.append(e)
    
    return list(map(int, answer))

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")) # return [2, 1, 3, 4]
print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")) # return [2, 1, 3, 4]
print(solution("{{20,111},{111}}")) # return [111, 20]
print(solution("{{123}}")) # return [2, 1, 3, 4]
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}")) # return [3, 2, 4, 1]