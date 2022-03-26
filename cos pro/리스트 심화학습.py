def solution1(late_table):
    answer = 0
    for x in late_table:
        if x >= 1 and x < 10:
            answer += 1000
        elif x >= 10 and x < 20:
            answer += 2000
        elif x >= 20 and x < 30:
            answer += 4000
        elif x >= 30:
            answer += 10000
    return answer


print(solution1([5, 0, 26, 14, 30, -7, 17, -3, -2, 5]))


def solution2(score):
    answer = 0
    count = 0
    for s in score:
        answer += s
        if s == 10:
            count += 1
    if count >= 7:
        answer += 100
    return answer


print(solution2([10, 9, 10, 6, 10, 10, 10, 7, 10, 10]))


def solution3(tasks):
    answer = 0
    counter1, counter2 = 0, 0
    for s in tasks:
        if s <= 4:
            counter1 += s*2
        else:
            counter2 += s*2

    if counter1 > counter2:     # 더 긴 시간이 전체 업무 처리시간
        answer = counter1
    else:
        answer = counter2
    return answer


print(solution3([7, 1, 4, 2, 3, 2, 5, 1]))
