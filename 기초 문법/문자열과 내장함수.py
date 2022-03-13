msg = "It is Time"
print(msg.upper())
print(msg.lower())
print(msg)

tmp = msg.upper()
print(tmp.find('T'))
print(tmp.count('T'))

for i in range(len(msg)):
    print(msg[i], end = ' ')
print()
for x in msg:
    print(x, end = ' ')
print()

for x in msg:
    if x.isupper():
        print(x,end=' ')
print()
for x in msg:
    if x.isalpha():     #알파벳이냐
        print(x,end=' ')
print()

tmp = 'AZ'
for x in tmp:
    print(ord(x))   #아스키넘버(A는 65 Z는 90)
    print(ord(x.lower()))

tmp = 65
print(chr(tmp)) #아스키넘버를 문자로 출력
