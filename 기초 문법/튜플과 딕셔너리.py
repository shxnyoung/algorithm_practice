#튜플
basket= ('apple','orange','pear')
basket = ('banana',)    #튜플 값 하나일 때 꼭 뒤에 콤마 붙여주기
x = ('1','2','3','4','5')
pos = x.index('3')  #튜플은 내용을 변경할 수 없는 데이터 타입이라 index(), count() 메소드만 사용 가능
print(pos,x[pos])

#딕셔너리
m = {"1반":27, "2반":28, "3반":27, "4반":30}    #키와 값의 쌍 (키는 중복값x, 변경 불가능), 자료 순서 없어서 인덱스 없음
print("1반")
for i in m:
    print(i, ":", m[i]) #i가 key값
m["3반"] =50
print(m)
