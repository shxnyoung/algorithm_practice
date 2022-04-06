
def solution(arr, k):
    answer = 0
    one_list = []
    # for i in arr:
    #     for j in i:
    #         one_list.append(j)
    for i in arr:
        one_list.extend(i)  # 배열 붙이기
    sorted_list = sorted(one_list)
    answer = sorted_list[k-1]
    return answer


# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
arr = [[5, 12, 4, 31], [24, 13, 11, 2], [43, 44, 19, 26], [33, 65, 20, 21]]
k = 4
ret = solution(arr, k)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret, " 입니다.")
