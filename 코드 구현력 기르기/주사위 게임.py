import sys
#sys.stdin = open("input.txt", "rt")
n = int(input())
max_price = 0
for i in range(n):
    a, b, c = map(int, input().split())
    price = 0
    if a == b == c:
        price = 10000 + a * 1000
    elif a == b and a != c:
        price = 1000 + a * 100
    elif a == c and a != b:
        price = 1000 + a * 100
    elif c == b and a != c:
        price = 1000 + c * 100
    elif a != b != c:
        price = max(a, b, c) * 100
    if price > max_price:
        max_price = price
print(max_price)

# 풀이 코드
# res = 0
# for i in range(n):
#     tmp = input().split()  # 문자화 된 숫자가 리스트로 tmp에 저장됨
#     tmp.sort()  # 가장 눈이 큰 숫자 찾기 위해서 오름차순 정렬
#     a, b, c = map(int, tmp)
#     if a == b and b == c:
#         money = 10000 + a*1000
#     elif a == b or a == c:
#         money = 1000 + a*100
#     elif b == c:
#         money = 100 + b*100
#     else:
#         money = c*100
#     if money > res:
#         res = money
# print(res)
