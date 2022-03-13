'''
1) 1부터 n까지 홀수 출력
2) 1부터 n까지 합 구하기
3) n의 약수 구하기
'''
n = int(input())
for i in range(1,n+1):
    if i % 2 != 0:
        print(i)


sum = 0
for i in range(1,n+1):
    sum += i
print(sum)



for i in range(1,n+1):
    if n % i == 0:
        print(i, end = " ")
