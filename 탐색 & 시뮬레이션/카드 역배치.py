import sys
#sys.stdin = open("input.txt", "rt")

a = list(range(21))
for _ in range(10):  # _를 넣어서 변수를 지정하지 않음, 그냥 반복만
    s, e = map(int, input().split())
    for i in range((e-s+1)//2):  # 값을 교환해주는 횟수가 (끝-앞 +1) //2
        a[s+i], a[e-i] = a[e-i], a[s+i]  # 파이썬의 swap
a.pop(0)  # 0번 인덱스 값을 pop
for x in a:
    print(x, end=' ')
