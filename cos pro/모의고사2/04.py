def solution(scores):
    grade_counter = [0 for i in range(5)]
    for x in scores:
        if 85 <= x <= 100:
            grade_counter[0] += 1
        elif 70 <= x <= 84:
            grade_counter[1] += 1
        elif 55 <= x <= 69:
            grade_counter[2] += 1
        elif 40 <= x <= 54:
            grade_counter[3] += 1
        else:
            grade_counter[4] += 1
    return grade_counter


# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
scores = [86, 72, 98, 60, 45]
ret = solution(scores)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret, " 입니다.")
