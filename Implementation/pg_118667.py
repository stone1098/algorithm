from collections import deque

def solution(queue1, queue2):
    answer = 0
    q1 = deque(queue1)
    q2 = deque(queue2)

    sum_q1 = sum(q1)
    sum_q2 = sum(q2)

    if (sum_q1+sum_q2)%2==1 or (sum_q1+sum_q2)==0:
        return -1
    
    max = len(q1) * 4

    for i in range(max):
        if sum_q1 > sum_q2:
            temp = q1.popleft()
            q2.append(temp)
            answer += 1
            sum_q1 -= temp
            sum_q2 += temp

        elif sum_q2 > sum_q1:
            temp = q2.popleft()
            q1.append(temp)
            answer += 1
            sum_q2 -= temp
            sum_q1 += temp
    
        else:
            return answer

    return -1