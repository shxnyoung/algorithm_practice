def solution(stones):
    cnt = 0
    current = 0
    n = len(stones)
    while current < n:
        current += stones[current]
        cnt += 1
    return cnt


# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
stones = [2, 5, 1, 3, 2, 1]
ret = solution(stones)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret, " 입니다.")
