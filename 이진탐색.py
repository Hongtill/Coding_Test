"""
# 이진탐색
- 어떤 값을 찾을 때, 정렬의 특징을 이용해 빨리 찾음
- 정렬되어 있을 경우, 어떤 값 찾을 때 : 전체 탐색 시, O(N) -> 이진 탐색 시, O(logN)
- 처음부터 이진탐색 문제라고 생각하기 어려움, 쉬운 방법부터 생각

# 핵심코드
def search(start, end, target) :
    if start == end :
        // ~~
        return
        
    mid = (start+end) // 2
    if nums[mid] < target :
        search(mid+1, end, target)
    else :
        search(start, mid, target)

# 초기 아이디어
- M개의 수마다 각각 어디에 있는지 찾기
- for : M개의 수
- for : N개의 수 안에 있는지 확인

# 초기 시간복잡도
- for : M개의 수 > O(M)
- for : N개의 수 안에 있는지 확인 > O(N)
- O(MN) : 1e10 > 시간초과

# 1. 아이디어
- M개를 확인해야 하는데, 연속하다는 특징 활용 가능? => 불가
- 정렬해서 이진탐색 가능?
- N개의 수 먼저 정렬
- M개의 수 하나씩 이진탐색으로 확인
- 이진탐색 안에서 마지막에 데이터 찾으면, 1을 출력 아니면 0을 출력

# 2. 시간복잡도
- N개의 수 정렬 : O(N*logN)
- M개의 수 이진탐색 : O(M*logN)
- O((N+M)logN) = 2e5 * 20 = 4e6 => 가능

# 3. 자료구조
- 탐색 대상 수 : int[]
- 모든 수 범위 : -2^31 ~ 2^31 > int 가능

- 탐색하려는 수 : int[]
- 모든 수 범위 : -2^31 ~ 2^31 > int 가능

# Tip) 
- 입력의 개수가 1E5 정도의 경우라면 이진탐색을 위해 정렬해서 탐색할 경우에 시간복잡도(O(N*logN)가 넘어가지 않기 때문에 의심
"""

import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
M = int(input())
target_list = list(map(int, input().split()))

nums.sort() # 정렬을 해야 이진탐색이 가능

def search(st,en,target) :
    if st == en :
        if nums[st] == target :
            print(1)
        else :
            print(0)
        return
    
    mid = (st+en) // 2
    if nums[mid] < target:
        search(mid+1, en, target)
    else :
        search(st, mid, target)


for each_target in target_list:
    search(0, N-1, each_target)
