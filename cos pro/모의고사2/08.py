def solution(name_list):
    answer = 0
    for name in name_list:
        for n in name:
            if n == 'j' or n == 'k':
                answer += 1
                break
    return answer


# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
name_list = ["james", "luke", "oliver", "jack"]
ret = solution(name_list)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret, " 입니다.")
