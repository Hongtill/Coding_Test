def solution(citations):

    # 1. 인용 횟수를 내림차순으로 정렬합니다.
    citations.sort(reverse=True)
    
    # 2. enumerate를 사용하여 논문 수(i+1)와 인용 횟수(citation)를 비교합니다.
    for i, citation in enumerate(citations):
        # h번 이상 인용된 논문이 h편 이상이어야 한다는 조건을 확인합니다.
        # 논문 편수(i+1)가 인용 횟수(citation)보다 커지는 순간,
        # 이전까지의 논문 편수(i)가 H-Index의 최댓값이 됩니다.
        if i + 1 > citation:
            return i
            
    # 3. 만약 위 반복문이 모두 통과했다면,
    # 모든 논문의 인용 횟수가 전체 논문 수보다 많거나 같은 경우입니다.
    # 이 경우 H-Index는 전체 논문의 수가 됩니다.
    return len(citations)
