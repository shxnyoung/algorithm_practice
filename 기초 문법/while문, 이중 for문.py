#주사위 수 맞추기
import random
k = random.randint(1,6)

while True:
    a = int(input("주사위 수는? "))


    if a == k:
        print("정답", k, a)
        break
    else:
        print("오답", k, a)

#구구단 출력 
for d in range(2, 10):
    for i in range(1, 10):
        print(d, 'x', i ,'=', d*i)
    print()
