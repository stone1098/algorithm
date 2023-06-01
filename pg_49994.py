def solution(dirs):

    move_list = []
    loc = [0, 0]

    for dir in dirs:
        if dir == 'U' and loc[1] + 1 <= 5:
            move_loc = [loc[0], loc[1] + 1]
            visit_line = sorted([loc, move_loc])
            move_list.append(visit_line)
            loc = move_loc
        elif dir == 'D' and loc[1] - 1 >= -5:
            move_loc = [loc[0], loc[1] - 1]
            visit_line = sorted([loc, move_loc])
            move_list.append(visit_line)
            loc = move_loc
        elif dir == 'R' and loc[0] + 1 <= 5:
            move_loc = [loc[0] + 1, loc[1]]
            visit_line = sorted([loc, move_loc])
            move_list.append(visit_line)
            loc = move_loc
        elif dir == 'L' and loc[0] - 1 >= -5:
            move_loc = [loc[0] - 1, loc[1]]
            visit_line = sorted([loc, move_loc])
            move_list.append(visit_line)
            loc = move_loc

    answer = []
    for move in move_list:
        if move not in answer:
            answer.append(move)

    return len(answer)

print(solution("ULURRDLLU")) # return 7
print(solution("LULLLLLLU")) # return 7