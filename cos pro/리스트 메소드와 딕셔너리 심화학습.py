def solution1(score):
    answer = []
    sort_score = sorted(score, reverse=True)  # 새로운 배열 객체 생성해서 정렬된 리스트 만들기

    for i in score:
        answer.append(sort_score.index(i)+1)  # i의 인덱스(순서)를 정렬된 리스트에서 가져와서 추가
    return answer


print(solution1([190, 183, 147, 183, 138, 133, 110, 145]))


def func_a(scores, score):
    rank = 1
    for s in scores:
        if s == score:
            return rank
        rank += 1
    return 0


def func_b(arr):
    arr.sort(reverse=True)


def func_c(arr, n):
    return arr[n]


def solution2(scores, n):
    score = func_c(scores, n)
    func_b(scores)
    answer = func_a(scores, score)
    return answer


scores = [190, 183, 147, 183, 138, 133, 110, 145]
print(solution2(scores, 2))


def func_d(cards):
    answer = 0
    scores = {'A': 1, 'B': 2, 'C': 3, 'D': 4}
    for card in cards:
        answer += scores[card]
    return answer


def func_e(cards, start):
    return cards[start::2]


def func_f(score1, score2):
    if score1 > score2:
        return [1, score1]
    elif score2 > score1:
        return [2, score2]
    else:
        return [0, score1]


def solution3(n, cards):
    person1 = func_e(cards, 0)[:n]  # 첫번째 사람이 받는 카드
    person2 = func_e(cards, 1)[:n]  # 두번째 사람이 받는 카드
    score1 = func_d(person1)
    score2 = func_d(person2)
    return func_f(score1, score2)


print(solution3(5, 'BCDAABCBADBBDACADCDB'))
