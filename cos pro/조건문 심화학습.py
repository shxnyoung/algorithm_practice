def solution1(height):
    answer = 0
    if height < 120 or height > 180:
        answer = '탑승불가'
    else:
        answer = '탑승가능'
    return answer


print(solution1(109))
print(solution1(120))


def solution2(p):
    answer = 0
    if p >= 500:
        answer = p // 100 * 100
    return answer


print(solution2(8925))


def solution3(f, n):
    answer = 0
    if f <= 10:
        answer = n * 3000
    elif 11 < f <= 20:
        answer = n*int(3000*11/10)
    else:
        answer = n*int(3000*12/10)
    return answer


print(solution3(5, 3))
print(solution3(15, 2))
print(solution3(21, 3))


def solution4(p):
    if p >= 101 and p <= 139:
        print("정상")
    else:
        print("비정상")


solution4(139)  # return 값 받지 않고 호출 가능해서 print() 안에 사용 안해도 됨
solution4(140)
