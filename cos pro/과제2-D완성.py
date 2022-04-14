# 2-D. 점수에 따른 순위를 매기는 프로그램

def solution(scores):
    # 과제1. 점수에 따른 순위가 저장된 리스트 answer를 return하기
    #    1. answer를 빈 리스트로 초기화 합니다.
    #    2. for문을 이용하여
    #       순위를 정해야할 점수의 인덱스를 순서대로 받아옵니다.
    #       2-1. 받아온 점수를 1등으로 초기화
    #       2-2. for문으 이용하여
    #            비교할 점수들을 순서대로 받아옵니다.
    #            2-2-1. 순위를 정할 점수가 비교할 점수보다 작으면
    #                   순위의 수를 1 증가시킵니다.
    #       2-3. 정해진 순위를 answer에 추가합니다.

    answer = []*len(scores)
    for i in range(len(scores)):
        max_score = scores[i]
        rank = 1
        for j in scores:
            if max_score < j:
                rank += 1
        answer.append(rank)
    return answer


# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
score1 = [90, 87, 87, 23, 35, 28, 12, 46]
ret1 = solution(score1)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret1, " 입니다.")

score2 = [10, 20, 20, 30]
ret2 = solution(score2)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret2, " 입니다.")
