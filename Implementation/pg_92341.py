def time_parse(time):
    h, m = map(int, time.split(':'))
    return h*60 + m
    
def solution(fees, records):
    answer = []
    number = dict()
    for r in records:
        number[r[6:10]] = 0
    number = dict(sorted(number.items()))
    
    for r in records:
        t, n, s = r.split(' ')
        t = time_parse(t)
        if s == 'IN':
            number[n] -= t
        else:
            number[n] += t
    
    close = time_parse('23:59')
    for n, t in number.items():
        if t <= 0:
            number[n] += close
            
    time_list = list(number.values())
    for t in time_list:
        if t <= fees[0]:
            answer.append(fees[1])
        else:
            temp = fees[1] + (t - fees[0]) // fees[2] * fees[3]
            if (t - fees[0])%fees[2] != 0:
                temp += fees[3]
            answer.append(temp)
    
    return answer

f = [180, 5000, 10, 600]
r = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
print(solution(f, r))