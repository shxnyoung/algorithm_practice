#리스트 표현식_조건문 

#for문으로 생성된 데이터 중에서 if문 만족하는 값 출력 
a = [i for i in range(10) if i % 3 == 0]
print(a)
a = list(i for i in range(10) if i % 3 == 0)
print(a)


a = [i for i in range(1,101) if i % 5 == 0]
b = [i for i in range(5,101,5)]
sum = sum(a)
print(sum)
 
