import sys
#sys.stdin = open("input.txt", "rt")

w = input()
n = ''
for i in w:
    if i.isdigit():
        n += i
    else:
        pass
n = int(n)
print(n)

cnt = 0
for i in range(1, n+1):
    if n % i == 0:
        cnt += 1
print(cnt)
