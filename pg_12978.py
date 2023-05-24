'''
N개의 마을로 이루어진 나라가 있습니다. 
이 나라의 각 마을에는 1부터 N까지의 번호가 각각 하나씩 부여되어 있습니다. 
각 마을은 양방향으로 통행할 수 있는 도로로 연결되어 있는데, 
서로 다른 마을 간에 이동할 때는 이 도로를 지나야 합니다. 
도로를 지날 때 걸리는 시간은 도로별로 다릅니다. 
현재 1번 마을에 있는 음식점에서 각 마을로 음식 배달을 하려고 합니다. 
각 마을로부터 음식 주문을 받으려고 하는데, 
N개의 마을 중에서 K 시간 이하로 배달이 가능한 마을에서만 주문을 받으려고 합니다.

마을의 개수 N, 각 마을을 연결하는 도로의 정보 road, 
음식 배달이 가능한 시간 K가 매개변수로 주어질 때, 
음식 주문을 받을 수 있는 마을의 개수를 return 하도록 solution 함수를 완성해주세요.



재귀를 이용한 탐색으로 해야될 거 같은데...
'''

def dfs(road, num, time):
    
    # 방문한 애들을 저장할 임시 테이블
    temp = []
    
    for r in road:
        if r[0] == num:
            temp.append(r[1])
            if time[r[1]] == 0:
                time[r[1]] = time[num] + r[2]
            else:
                if time[r[1]] > time[num] + r[2]:
                    time[r[1]] = time[num] + r[2]
                
    for t in temp:
        dfs(road, t, time)                    

def solution(N, road, K):
    answer = 0
    
    for r in road:
        if r[0] > r[1]: r[0], r[1] = r[1], r[0]

    # 1부터 시간이 얼마나 걸리는 지 작성
    time = [0] * (N+1)
    
    dfs(road, 1, time)

    for i in range(1, len(time)):
        if time[i] <= K: answer+=1

    return answer

road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
print(solution(5, road, 3)) # return 4

road = [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]]
print(solution(6, road, 4)) # return 4