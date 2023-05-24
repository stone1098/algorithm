# def solution(numbers):
#     answer = []
    
#     for n in numbers:
#         for i in range(n+1, 10**15):
#             other = bin(n^i).count('1')
#             if other < 3:
#                 answer.append(i)
#                 break
#     return answer

def solution(numbers):
    answer = []
    
    for n in numbers:
        if n % 2 == 0:
            answer.append(n+1)
        else: