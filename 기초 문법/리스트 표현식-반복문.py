#리스트 표현식_반복문

#1)특정 값으로 초기화된 리스트 생성하기
a = [0 for _ in range(5)]
a = [0 for i in range(5)]
b = [0] * 5
print(a)
print(b)

#2)range값을 값으로 갖는 리스트 생성하기
a = [i for i in range(5)]
print(a)
a = list(i for i in range(3,10,2))
print(a)
c = []
for i in range(5):
    c.append(i)
print(c)
b = []
for i in range(5):
    b += [i]
print(b)

#3) 연산을 적용한 값으로 리스트 생성
a = [str(i+10) for i in range(0,20,3)]
print(a)
c = []
for i in range(5):
    c.append(str(i+10))
print(c)
b = []
for i in range(5):
    b += [str(i+10)]
print(b)
