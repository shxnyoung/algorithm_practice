import sys
#sys.stdin = open("input.txt", "rt")

n = int(input())
lst = list(map(int, input().split()))

score = 0
continue_score = 0
for i in lst:
    if i == 1:
        continue_score += 1
        score += continue_score
    if i == 0:

        continue_score = 0
print(score)
