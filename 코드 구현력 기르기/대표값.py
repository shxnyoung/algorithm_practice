import sys
#sys.stdin = open("input.txt", "rt")

n = int(input())
score = list(map(int, input().split()))
#avg = round(sum(score)/n)
# st_num = 0
# c = 100
# for i in range(n):
#     i_c = abs(avg - score[i])
#     if c > i_c:
#         st_num = i
#         c = i_c
#     if c == i_c:
#         if score[st_num] < score[i]:
#             st_num = i
#             #print("p", st_num, i+1)
#         elif score[st_num] == score[i]:
#             st_num = min(st_num, i)
# print(avg, st_num+1)

avg = int(sum(score)/n + 0.5)
min = 21000000
for idx, x in enumerate(score):
    tmp = abs(x - avg)
    if tmp < min:
        min = tmp
        score = x
        res = idx + 1  # 실제 학생번호
    elif tmp == min:
        if x > score:
            score = x
            res = idx + 1
print(avg, res)
