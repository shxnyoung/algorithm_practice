import sys
#sys.stdin = open("input.txt", "rt")

n, k = map(int, input().split())
num = list(map(int, input().split()))

res = set()  # set: 중복값 제거하는 자료구조
for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            res.add(num[i]+num[j]+num[m])
res = list(res)  # set 자료구조는 sort를 사용할 수 없어서 list로 바꿔줌
res.sort(reverse=True)
print(res[k-1])
