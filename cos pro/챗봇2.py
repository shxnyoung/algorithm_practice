import random

greet=['안녕','하이','hi']
age = ['나이','몇 살','년생']
song = ['노래','음악','가수']

while True:
    w = input(">>")
    if w == 'q':
        break
    for a in greet + age + song:
        if a in greet and a in w:
            print(random.choice(['안녕하세요','hello','하이']))
            break
        elif a in age and a in w:
            print(random.choice(['비밀인데','24살이야','그건 왜','1999년생이야']))
            break
        elif a in song and a in w:
            print(random.choice(['에드시런 어때','블랙핑크가 짱이야','노래 몰라']))
            break
        
