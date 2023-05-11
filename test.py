report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]

report_list = []
for _ in range(4):
    report_list.append(set())

temp = [set() for _ in range(4)]

report_list[0].add(1)
temp[0].add(1)

print(report_list)
print(temp)