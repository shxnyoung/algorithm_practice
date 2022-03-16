import sys
#sys.stdin = open("input.txt", "rt")

n1 = int(input())
arr1 = list(map(int, input().split()))
n2 = int(input())
arr2 = list(map(int, input().split()))

# 포인터 변수
p1 = p2 = 0

# 합해줄 리스트
arr = []

while p1 < n1 and p2 < n2:  # 하나의 포인터가 리스트 끝까지 갈 때 까지
    if arr1[p1] <= arr2[p2]:
        arr.append(arr1[p1])
        p1 += 1
    else:
        arr.append(arr2[p2])
        p2 += 1

# 다 안끝난 리스트의 뒷부분을 붙여주기
if p1 < n1:
    arr = arr + arr1[p1:]
if p2 < n2:
    arr = arr + arr2[p2:]

for x in arr:
    print(x, end=' ')


# 방법 2(비추천)
# arr = arr1 + arr2
# arr.sort()  # 시간복잡도 nlogn
# for i in arr:
#     print(i, end=' ')
