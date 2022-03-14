a = [0] * 10
print(a)
a = [[0]*3 for _ in range(3)]   #가로가 행 세로가 열
print(a)
a[0][1] = 1     #0행 1열
print(a)
a[1][1] = 2
print(a)

#표처럼 출력
for x in a: #각 행마다 출력
    print(x)
        
for x in a:
    for y in x:
        print(y, end = ' ')
    print()
