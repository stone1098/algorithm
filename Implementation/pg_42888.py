# https://school.programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    answer = list()
    id_dict = dict()
    action_list = list()

    for r in record:
        temp = r.split(' ')

        if temp[0] == 'Enter':
            id_dict[temp[1]] = temp[2]
            action_list.append([temp[1], temp[0]])
        elif temp[0] == 'Change':
            id_dict[temp[1]] = temp[2]
        elif temp[0] == 'Leave':
            action_list.append([temp[1], temp[0]])

    action_dict = {'Enter' : '들어왔습니다.', 'Leave' : '나갔습니다.'}

    for a in action_list:
        answer.append(f"{id_dict.get(a[0])}님이 {action_dict.get(a[1])}")

    return answer

record = "Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"
print(solution(record)) # return ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]