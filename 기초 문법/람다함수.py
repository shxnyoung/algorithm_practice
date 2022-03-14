#람다 함수 = 익명의 함수


def plus_one(x):
    return x + 1

print(plus_one(1))


plus_two = lambda x : x+2  #매개변수 x에 2를 더해서 x+2를 리턴함, 변수에 할당해줘야 함
print(plus_two(1))

a = [1,2,3]
print(list(map(plus_one,a)))    #map(함수명, 자료)
print(list(map(lambda x : x+1,a)))
