# 2-C. 시험에 합격한 인원을 구하는 프로그램

#      각 사람별 세 과목의 점수가 주어졌을 때,
#          A과목은 80점 이상,
#          B과목은 90점 이상,
#          C과목은 70점 이상이면 합격
#      합격한 과목이 하나 이하거나,
#      합격 점수의 반을 넘기지 못한 과목이 있다면 불합격.
#

# 과제1. 함수명의 정의하기

# 1. 합격한 과목이 몇 개인지 구하는 함수를 찾아
#   함수명을 func_ok로 지정합니다.

# 2. 합격 점수의 반을 넘기지 못한 과목이 몇 개인지 구하는 함수를 찾아
#   함수명을 func_non_ok으로 지정합니다.

# 3. 합격한 과목이 하나보다 많고
#   합격 점수의 반을 넘기지 못한 과목이 없으면
#   합격한 인원에 포함시키는 함수는 찾아
#   함수명을 func_passed로 지정합니다.

def func_passed(ok_num, non_ok_num):
    return (ok_num > 1 and non_ok_num == 0)


def func_non_ok(s):
    answer = 0
    if s[0] < 40:
        answer += 1
    if s[1] < 45:
        answer += 1
    if s[2] < 35:
        answer += 1
    return answer


def func_ok(s):
    answer = 0
    if s[0] >= 80:
        answer += 1
    if s[1] >= 90:
        answer += 1
    if s[2] >= 70:
        answer += 1
    return answer


# 과제 2. 각 과목 점수를 담고 있는 리스트가 매개변수로 주어질 때,
#        시험에 합격한 인원수를 구하는 프로그램을
#        함수를 호출하여 완성하기

# 1. 합격한 과목이 몇 개인지 구하는 함수를 호출하여
#   그 리턴값을 ok라는 변수에 저장합니다.

# 2. 합격 점수의 반을 넘기지 못한 과목이 몇 개인지 구하는 함수를 호출하여
#   그 리턴값을 non_ok라는 변수에 저장합니다.

# 3. 합격한 종목이 하나보다 많고
#   합격 점수의 반을 넘기지 못한 과목이 없으면
#   합격한 인원에 포함시키는 함수를 호출하여
#   그 결과를 answer에 더합니다.

def solution(scores):
    answer = 0
    for s in scores:
        ok = func_ok(s)
        non_ok = func_non_ok(s)
        answer += func_passed(ok, non_ok)
    return answer


# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
scores1 = [[30, 40, 100], [97, 88, 95]]
ret1 = solution(scores1)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

scores2 = [[90, 88, 70], [85, 90, 90], [100, 100, 70],
           [30, 90, 80], [40, 10, 20], [83, 88, 80]]
ret2 = solution(scores2)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")
