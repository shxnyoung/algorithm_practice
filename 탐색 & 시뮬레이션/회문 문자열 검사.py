import sys
#sys.stdin = open("input.txt", "rt")

n = int(input())


def fbsame(x):
    x = x.lower()
    rx = str(x)[::-1]
    #print(x, rx)
    if x == rx:
        return "YES"
    else:
        return "NO"


for i in range(n):
    word = str(input())
    res = fbsame(word)
    print("#", i+1, " ", res, sep='')


# 방법 2
# for i in range(n):
#     s = input()
#     s = s.upper()
#     size = len(s)
#     for j in range(size // 2):
#         if s[j] != s[-1-j]:
#             print("#%d NO" %(i+1))
#             break
#     else:
#         print("#%d YES" %(i+1))

# 방법 3
# for i in range(n):
#     s = input()
#     s = s.upper()
#     if s == s[::-1]:
#         print("#%d YES" %(i+1))
#     else:
#         print("#%d NO" %(i+1))
