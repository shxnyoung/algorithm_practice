import sys
#sys.stdin = open("input.txt", "rt")
n = int(input())
arr = list(map(int, input().split()))


def reverse(x):
    s = str(x)
    rev_s = s[::-1]
    return int(rev_s)


# def reverse(x):
#     res = 0
#     while x > 0:
#         t = x % 10
#         res = res*10 + t
#         x = x//10
#     return res


def isPrime(x):
    if x == 1:
        return False
    for i in range(2, int(x**(1/2))+1):
        if x % i == 0:
            return False
    return True


for i in arr:
    tmp = reverse(i)
    if isPrime(tmp):
        print(tmp, end=' ')
