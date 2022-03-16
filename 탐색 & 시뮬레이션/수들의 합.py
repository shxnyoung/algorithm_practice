import sys
#sys.stdin = open("input.txt", "rt")
n, m = map(int, input().split())
a = list(map(int, input().split()))


# 포인터 변수(인덱스를 가리킴)
lt = 0
rt = 1
tot = a[0]
cnt = 0

while True:
    if tot < m:  # rt를 오른쪽으로 이동시킴
        if rt < n:
            tot += a[rt]
            rt += 1
        else:  # rt가 마지막까지 갔을 때 반복 중단
            break
    elif tot == m:  # lt를 오른쪽으로 이동시킴
        cnt += 1
        tot -= a[lt]
        lt += 1
    else:  # tot > m일 때 lt를 오른쪽으로 이동시킴
        tot -= a[lt]
        lt += 1
print(cnt)
