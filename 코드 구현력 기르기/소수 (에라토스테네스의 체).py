import sys
#sys.stdin = open("input.txt", "rt")

n = int(input())
arr = [0] * (n+1)  # n+1까지 해야 20까지 인덱스가 생성됨
cnt = 0  # range를 2부터 시작해서 맨 처음 arr[0],arr[1]은 소수에서 제외 안함
for i in range(2, n+1):
    if arr[i] == 0:
        cnt += 1
    # 방법1 (1초 시간제한 초과)
    # for j in range(i, n+1):
    #     # i의 배수들을 체에 걸러준다
    #     if j % i == 0:
    #         arr[j] += 1
    # 방법2 (시간제한 성공)
    for j in range(i, n+1, i):
        # i의 배수들을 체에 걸러준다
        arr[j] += 1

print(cnt)
