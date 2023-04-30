'''
어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자를 구하려 합니다.

예를 들어, 숫자 1924에서 수 두 개를 제거하면 [19, 12, 14, 92, 94, 24] 를 만들 수 있습니다. 이 중 가장 큰 숫자는 94 입니다.

문자열 형식으로 숫자 number와 제거할 수의 개수 k가 solution 함수의 매개변수로 주어집니다. 
number에서 k 개의 수를 제거했을 때 만들 수 있는 수 중 가장 큰 숫자를 문자열 형태로 return 하도록 solution 함수를 완성하세요.


'''
def solution(number, k):

    answer = ''
    answer_len = len(number) - k
    idx = 0

    for i in range((answer_len-1), 0, -1):
        max_num = max(number[idx:-i])
        answer += max_num
        number = number[number.index(max_num)+1:]
    answer += max(number)

    return answer

# print(solution('1924', 2)) # return 94
print(solution("1231234", 3)) # return 3234
print(solution("4177252841", 4)) # return 775841