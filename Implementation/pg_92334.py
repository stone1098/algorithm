'''
각 유저는 한 번에 한 명의 유저를 신고할 수 있습니다.
- 신고 횟수에 제한은 없습니다. 서로 다른 유저를 계속해서 신고할 수 있습니다.
- 한 유저를 여러 번 신고할 수도 있지만, 동일한 유저에 대한 신고 횟수는 1회로 처리됩니다.

k번 이상 신고된 유저는 게시판 이용이 정지되며, 해당 유저를 신고한 모든 유저에게 정지 사실을 메일로 발송합니다.
- 유저가 신고한 모든 내용을 취합하여 마지막에 한꺼번에 게시판 이용 정지를 시키면서 정지 메일을 발송합니다.

이용자의 ID가 담긴 문자열 배열 id_list, 
각 이용자가 신고한 이용자의 ID 정보가 담긴 문자열 배열 report, 
정지 기준이 되는 신고 횟수 k가 매개변수로 주어질 때, 
각 유저별로 처리 결과 메일을 받은 횟수를 배열에 담아 return 하도록 solution 함수를 완성해주세요.

1. report에서 신고자와 피신고자를 추출
2. 리스트 안에 set형태로 신고한 목록 저장
3. 피신고자 리스트에서 k를 넘는 애들만 정지 (인덱스만 추출?) -> 정지 리스트
4. 정지 리스트 안에 내가 신고한 애들만 뽑아 len 출력
'''

def solution(id_list, report, k):

    member_len = len(id_list)

    report_list = []
    for _ in member_len:
        report_list.append(set())

    for r in report:
        reporter, respondent = r.split(" ")

        repoter_idx = id_list.index(reporter)
        respondent_idx = id_list.index(respondent)

        report_list[repoter_idx].add(respondent_idx)
    
    # 신고 횟수 뽑기 ex) [{1, 3}, {3}, {0, 1}, set()]
    ban_list = [0] * member_len
    for element in report_list:
        for e in element:
            ban_list[e] += 1

    # 정지 리스트 뽑기
    temp = set()
    for i in range(member_len):
        if ban_list[i] >= k:
            temp.add(i)

    # 신고한 애들과 정지 리스트의 교집합을 구함
    answer = []
    for r in report_list:
        answer.append(len(r & temp))

    return answer


id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

print(solution(id_list, report, k)) # return [2, 1, 1, 0]

id_list = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 3

print(solution(id_list, report, k)) # return [0, 0]