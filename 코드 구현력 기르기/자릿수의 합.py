import sys
#sys.stdin = open("input.txt", "rt")

n = input()
lst = list(map(int, input().split()))


def digit_sum(i):
    sum = 0
    while i != 0:
        sum += (i % 10)
        i = i // 10
    return sum

# 파이썬에서의 쉬운 방법
# def digit_sum(x):
#     sum = 0
#     for i in str(x):
#         sum += int(i)
#     return sum


maxsum = 0

for i in lst:
    total = digit_sum(i)

    if total > maxsum:
        maxsum = total
        maxnum = i
print(maxnum)
