def solution(height, k):
    answer = 0
    n = len(height)
    for h in height:
        if h > k:
            answer += 1
    return answer


# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
height = [165, 170, 175, 180, 184]
k = 175
ret = solution(height, k)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret, " 입니다.")
