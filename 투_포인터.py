""" 
# 투 포인터
- 각 원소마다 모든 값을 순회해야 할 때 O(N^2)
- 연속하다는 특성을 이용해서 처리, O(N)
- 2개의 포인터(커서)가 움직이면서 계산
- 처음부터 생각하기 어려움, 쉬운 방법부터 생각

# 초기 아이디어 
- for문으로 각 숫자의 위치에서 이후 K개의 수를 더함
- 이 때마다 최대값으로 갱신

# 초기 시간복잡도
- for 문 : O(N)
- 각 위치에서 K개의 값을 더함 : O(K)
- 총 : O(NK)

# 아이디어
- 투 포인터를 활용
- 처음에 K개의 값을 구함
- for문 : 다음 인덱스의 값을 더하고, 이전 인덱스의 값을 뺌
- 이 때 최대값을 갱신

# 시간복잡도
- 숫자 개수만큼 for => O(N)
- O(N) = 1e5 => 가능

# 자료구조
- 전체 정수 배열 : int[] (가능한 모든 수가 -100~100 => int 가능)
- 합한 수 : int (100 * 1e5 = 1e7 => int 가능)
- 최대값 : int
"""

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
nums = list(map(int, input().split()))
each = 0

# K개를 더해주기
for i in range(K) :
    each += nums[i]

maxv = each

# 다음 인덱스 더해주고, 이전 인덱스 빼주기
for i in range(K, N) :
    each += nums[i]
    each -= nums[i-K]
    maxv = max(maxv, each)

print(maxv)
