import random as r
#리스트는 변수를 여러개 붙여둔거
#빈 리스트
a = []
b = list()

a = [1,2,3,4,5]
b = list(range(1,11))
c = a+b

print(a)
a.append(6) #맨 뒤에 값 추가
print(a)
a.insert(3,7)   #특정 인덱스에 특정 값 추가
print(a)

a.pop() #맨 뒷 값 제거
print(a)
a.pop(3)    #특정 인덱스 값의 값 제거
print(a)

a.remove(4) #특정 값 찾아서 제거
print(a)

print(a.index(5))   #특정 값의 인덱스 값 출력

print(sum(b))
print(max(b))
print(min(b))

r.shuffle(b)    #리스트를 무작위로 섞기 (random)
print(b)

b.sort()    #오름차순 정렬
print(b)
b.sort(reverse = True)  #내림차순 정렬
print(b)

b.clear()   #빈 리스트로
print(b)




a = [23,12,36,53,19]
print(a[:3])

for i in range(len(a)):
    print(a[i], end = ' ')
print()

for x in a:
    print(x, end = ' ')
print()


#튜플
b = (1,2,3,4,5) #튜플은 값 변경 불가

for x in enumerate(a):  #enumerate는 인덱스 번호와 값을 묶어서 튜플형태로 x에 넘김 
    print(x)

for x in enumerate(a):
    print(x[0], x[1])
print()

for index, value in enumerate(a):
    print(index, value)


if all(60 > x for x in a):   #for 문의 x값을 하나씩 조건문에 대입(60과 비교)해서 all 함수로 참 거짓 판별
    #모두 참이면 true, 하나라도 거짓이면 false
    print("Yes")
else:
    print("No")
    
    
if any(15 > x for x in a):   #한번만 참이면 true, 모두 거짓이면 false
    print("Yes")
else:
    print("No")

