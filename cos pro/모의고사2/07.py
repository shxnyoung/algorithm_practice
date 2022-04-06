def solution(s):
    s_lst = list(s)
    n = len(s)
    for i in range(n):
        if s_lst[i] == 'a':
            s_lst[i] = 'z'
        elif s_lst[i] == 'z':
            s_lst[i] = 'a'
    return "".join(s_lst)


# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
s = "abz"
ret = solution(s)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret, " 입니다.")
