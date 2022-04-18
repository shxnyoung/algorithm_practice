def func_a(cur_sale, pre_sale, rank, max_up):
    sale_len = len(cur_sale)
    count = 0
    for i in range(sale_len):
        if cur_sale[i] >= 70 and rank[i] <= sale_len // 5:
            count += 1
        elif cur_sale[i] >= 70 and rank[i] == 1:
            count += 1
        elif max_up > 0 and max_up == cur_sale[i] - pre_sale[i]:
            count += 1
    return count


def func_b(cur_sale, pre_sale):
    max_up = 0
    for i in range(len(cur_sale)):
        max_up = max(max_up, cur_sale[i] - pre_sale[i])
    return max_up


def func_c(cur_sale):
    sale_len = len(cur_sale)
    rank = [1] * sale_len
    for i in range(sale_len):
        for j in range(sale_len):
            if cur_sale[i] < cur_sale[j]:
                rank[i] += 1
    return rank


def solution(cur_sale, pre_sale):
    rank = func_c(cur_sale)
    max_up = func_b(cur_sale, pre_sale)
    answer = func_a(cur_sale, pre_sale, rank, max_up)
    return answer


# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
cur_month = [20, 50, 35, 80, 75]
pre_month = [15, 55, 75, 85, 75]
ret = solution(cur_month, pre_month)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
