# 다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(shirt_size):
    # 여기에 코드를 작성해주세요.
    answer = [0, 0, 0, 0, 0, 0]
    for i in shirt_size:
        if i == "XS":
            answer[0] += 1
        elif i == "S":
            answer[1] += 1
        elif i == "M":
            answer[2] += 1
        elif i == "L":
            answer[3] += 1
        elif i == "XL":
            answer[4] += 1
        elif i == "XXL":
            answer[5] += 1
    return answer


# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
shirt_size = ["XS", "S", "L", "L", "XL", "S"]
ret = solution(shirt_size)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret, " 입니다.")
