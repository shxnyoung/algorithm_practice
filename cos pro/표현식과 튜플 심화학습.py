def solution1(cleaning):
    answer = []
    for room, ox in enumerate(cleaning):
        if ox == 'X':
            answer.append(room+1)
    return answer


print(solution1(["O", "X", "X", "O", "O", "X", "O", "O", "X", "X"]))


def func_a(sales1, sales2):
    answer = 0
    for s1, s2 in zip(sales1, sales2):
        answer = max(answer, s2-s1)
    return answer


def func_b(sales1, sales2):
    answer = 0
    for s1, s2 in zip(sales1, sales2):
        answer = min(answer, s2-s1)
    return answer


def solution2(pre_month, cur_month):
    up = func_a(pre_month, cur_month)
    down = func_b(pre_month, cur_month)
    answer = [up, down]
    return answer


print(solution2([20, 50, 35], [15, 55, 75]))
print(solution2([20, 65, 77], [15, 55, 75]))


def solution3(words):
    answer = 0
    for i in words:
        rev_words = i[::-1]
        if i == rev_words:
            answer += 1

    return answer

# 다른 방법


def solution3_1(words):
    answer = len(words)
    for word in words:
        for wd, wr in zip(word, reversed(word)):
            if wd != wr:
                answer -= 1
                break
    return answer


def solution3_2(words):  # word의 절반을 나머지 절만의 뒤쪽부터 비교
    answer = len(words)
    for word in words:
        for i in range(len(word)//2):
            if word[i] != word[-i-1]:
                answer -= 1
    return answer


print(solution3(['banana', 'SOS', 'rotator', 'hello']))
