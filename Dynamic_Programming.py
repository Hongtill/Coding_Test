""" 
# DP
- Dynamic Programming
- 이전의 값을 재활용하는 알고리즘
- 예시 : 1~10 숫자 중, 각각 이전값들을 합한 값 구하기
- 이전의 값을 활용해서 시간복잡도 줄일 수 있음
- 점화식 : An = An-1 + An-2

# 1. 아이디어 
- A1 : 1, A2 : 2, A3 : 1+2
- An = A(n-1) + A(n-2)
- for문으로 3부터 N까지 돌면서
- 이전값과, 그 이전값을 더해서 10007로 나눈 값을 저장

# 2. 시간복잡도
- for : N => O(N)

# 3. 자료구조
- DP값을 저장하는 경위의 수 배열(An) : int[]
    - 최대값 : 10006 => int 가능
    
# Tip)
- 어떻게 할지 모르겠을 때는, 하나씩 그려보면서 규칙 찾기
- 점화식을 명확하게 세우고 코드 짜기
"""

import sys
input = sys.stdin.readline

n = int(input())
rs = [0,1,2]

for i in range(3, N+1) : 
    rs.append((rs[i-1] + rs[i-2] % 10007))
    
print(rs[n])
