# def solution1(d_day):
#     answer = 0
#     for i in range(1, d_day):
#         i = i+2
#         if i % 7 == 6:
#             answer += 1
#     return answer

# 정답
def solution1(d_day):
    answer = 0
    for i in range(1, d_day+1):  # 마지막 일자까지 포함해서 반복문 수행하도록
        if i % 7 == 6:
            answer += 1
    return answer


print(solution1(100))
print(solution1(13))


def solution2(n1, n2):
    answer = 0
    for i in range(n1, n2+1):
        answer += i
    return answer


print(solution2(11, 50))
print(solution2(31, 75))


# 최소공배수 구하는 방법1
def solutino_gcd(p, s):
    answer = 0
    for i in range(1, p*s+1):
        if i % p == 0 and i % s == 0:
            answer = i
            break
    return answer


print(solutino_gcd(4, 6))

# 최소공배수 구하는 방법 2


def solution3(p, s):
    answer = 0
    for i in range(1, s+1):
        if (p*i) % s == 0:
            answer = i*p
            break
    return answer


print(solution3(4, 6))
print(solution3(6, 10))


def solution3_1(p, s):
    answer = 0
    i = 1
    while(p*i) % s != 0:
        i += 1
    answer = p*i
    return answer


print(solution3_1(4, 6))
