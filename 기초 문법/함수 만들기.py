def add(a,b):
    c = a + b
    d = a-b
    return c,d    #값 반환, 여러 개의 값을 리턴할 때는 튜플 형태로


x = add(3,2)
print(x)


def isPrime(x):
    for i in range(2,x):
        if x % i == 0:
            return False
    return True

a = [12, 13, 7, 9, 19]
for x in a:
    if isPrime(x):
        print(x, end = ' ')
