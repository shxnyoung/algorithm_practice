def solution1(num1, num2):
    answer = num1+num2
    return answer


print(solution1(4, 5))


def solution2(num1, num2):
    answer = int(num1)+int(num2)
    return answer


print(solution2("4", "5"))


def solution3(n):
    a1 = n*5
    a2 = n*2
    a3 = n*3
    return a1, a2, a3


print(solution3(12))


def solution4(n):
    answer = 0, 0
    answer = 8 // n, 8 % n
    return answer


print(solution4(5))


def solution5(word):
    answer = word[-1]
    return answer


print(solution5('apple'))


def solution6(cards):
    answer = cards[1:10:2]
    return answer


print(solution6('GADUBFYIJKCLMNEPQVRHWSOXTZ'))


def solution7(word, start):
    answer = word[start:start+3]
    return answer


print(solution7("BINGO", 1))
