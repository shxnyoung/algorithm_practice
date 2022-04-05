def solution(number):
    count = 0
    for i in range(1, number + 1):
        current = i
        while current != 0:
            if current % 10 == 3 or current % 10 == 6 or current % 10 == 9:
                count += 1
            current = current // 10
    return count


# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
number = 40
ret = solution(number)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
