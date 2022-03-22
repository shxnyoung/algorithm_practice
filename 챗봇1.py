import webbrowser

print("안녕하세요 ~ 상담봇입니다 ~")

while True:
    quest=input("궁금하신 내용을 적어주세요")
    if '환불' in quest:
        print("고객님~ 환불을 원하실 경우에는 111-1111로 전화주세요")
    elif '교환' in quest:
        print("교환을 원하시면 7일 이내 반송 신청 해주시면 감사하겠습니다")
    else:
        print("고객님 죄송합니다. 이 질문에는 대답할 수가 없습니다")
        webbrowser.open("http://naver.com")
        break
    
        
    
