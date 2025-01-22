""" 
# 그리디
- 현재 차례의 최고의 답을 찾는 문제
- 어려운 이유 : 증명하기가 어려움
- ex) 다른 금액의 동전이 여러 개 주어졌을 때, M원을 만드는 최소의 개수

# 아이디어 
- 큰 금액의 동전부터 차감
- 반례? : 동전의 개수가 무한대라서 없는 것으로 보임
- K를 동전 금액으로 나눈 뒤, 남은 값으로 갱신

# 시간복잡도
- 동전의 개수만큼 for문 
- for : N > O(N)

# 자료구조
- 동전금액 : int[]
- 최대값 : 1e6 => int 가능
- 현재 남은 금액 : int
- 최대값 : 1e8 => int 가능
- 동전 갯수 : int
- 최대값 : 1e8 => int 가능

# 1. 아이디어
- 동전을 저장한 뒤, 반대로 뒤집음
- 동전 for >
    - 동전 사용 개수 추가
    - 동전 사용한만큼 K값 갱신
    
# 2. 시간복잡도
- O(N)

# 3. 자료구조
- 동전 금액 : int[]
- 동전 사용 cnt : int
- 남은 금액 : int

# Tip)
- 실전문제에서, 그리디로 푸는 문제임을 생각하기가 어려움
- 그리디 사용 이유 설명 or 반례 찾기 연습
"""

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
coins.reverse()
cnt = 0

for each_coin in coins :
    cnt += K // each_coin
    K = K % each_coin

print(cnt)
