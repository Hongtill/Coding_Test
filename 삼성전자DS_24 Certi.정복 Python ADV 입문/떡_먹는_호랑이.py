D, K = map(int, input().split())

def find_initial_values(K, D):
    # 첫날 A와 둘째 날 B의 값을 탐색
    for A in range(1, K+1):  # A는 1 이상 K 이하
        for B in range(A, K+1):  # B는 A 이상 K 이하
            # 첫날 A, 둘째 날 B에 대해 떡의 개수를 계산
            d1, d2 = A, B
            for day in range(3, D+1):  # D일째까지 계산
                d3 = d1 + d2  # 새로운 떡의 개수
                d1, d2 = d2, d3  # d1은 d2로, d2는 d3로 갱신
            if d2 == K:  # D일째 떡의 개수가 K와 같으면
                return A, B
            
#             print(d1, d2)
    return -1, -1


A, B = find_initial_values(K, D)
print(A)
print(B)
