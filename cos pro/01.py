size_kinds = 6


def func_a(shoes):
    count = [0 for _ in range(size_kinds)]
    for x in shoes:
        count[(x-210)//10] += 1
    return count


def solution(left_shoes, right_shoes):
    left_count = func_a(left_shoes)
    right_count = func_a(right_shoes)

    pair = 0
    for i in range(size_kinds):
        pair += min(left_count[i], right_count[i])
    return pair


# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
left_shoes = [210, 210, 220, 220, 230, 230,
              240, 250, 260, 230, 240, 210]

right_shoes = [230, 250, 220, 220, 230, 250,
               210, 230, 240, 250, 230, 240]

ret = solution(left_shoes, right_shoes)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
