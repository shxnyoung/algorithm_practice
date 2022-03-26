def func_a(n1, n2):
    answer = n1+n2
    return answer


def func_b(n1, n2):
    answer = n1*n2
    return answer


def solution1(num1, num2):
    plus = func_a(num1, num2)
    multi = func_b(num1, num2)
    answer = plus+multi
    return answer


print(solution1(4, 5))


def solution2(s1, s2):
    all_len = len(s1+s2)
    return all_len


print(solution2('pine', 'apple'))


def solution3(price, payment):
    change = max(-1, payment-price)
    return change


print(solution3(1400, 2000))
print(solution3(2100, 2000))


def solution4(score1, score2):
    answer = int((score1+score2)/2)
    return answer


print(solution4(2, 3))
