def func_a(k):
    sum = 0
    for i in range(1, k+1):
        sum += i

    return sum


def solution(n, m):
    sum_to_m = func_a(m)
    sum_to_n = func_a(n-1)
    answer = sum_to_m - sum_to_n
    return answer


# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
n1 = 5
m1 = 10
ret1 = solution(n1, m1)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret1, " 입니다.")

n2 = 6
m2 = 6
ret2 = solution(n2, m2)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret2, " 입니다.")
