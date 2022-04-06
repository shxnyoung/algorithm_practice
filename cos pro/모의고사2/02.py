def func_a(s):
    ret = 0
    for i in s:
        if i > ret:
            ret = i
    return ret


def func_b(s):
    ret = 0
    for i in s:
        ret += i
    return ret


def func_c(s):
    ret = 101
    for i in s:
        if i < ret:
            ret = i
    return ret


def solution(scores):
    sum = func_b(scores)
    max_score = func_a(scores)
    min_score = func_c(scores)
    return sum - max_score - min_score


# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
scores = [50, 35, 78, 91, 85]
ret = solution(scores)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret, " 입니다.")
