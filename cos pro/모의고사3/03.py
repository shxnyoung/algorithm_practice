import math

def solution(scores):
    scores.sort()
    nomin_scores = scores[1:-1]
    print(nomin_scores)
    answer = round(sum(nomin_scores)/len(nomin_scores))
    return answer


# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
scores = [90, 80, 70, 85, 100, 90]
ret = solution(scores)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
