"""
# 시뮬레이션
- 각 조건에 맞는 상황을 구현하는 문제
- 별도의 알고리즘 없이 풀 수 있으나, 구현력 중요
- 매 시험마다 1문제 이상 무조건 출제
- ex) 지도 상에서 이동하면서 탐험하는 문제, 배열 안에서 이동하면서 탐험하는 문제 

# 1. 아이디어
- 특정 조건 만족하는 한 계속 이동 -> While
- 4방향 탐색 먼저 수행 > 빈칸 있을 경우 이동
- 4방향 탐색 안될 경우, 뒤로 한칸 가서 반복

# 2. 시간복잡도
- while문 최대 : N x M 
- O(NM) : 50^2 = 2500 < 2억 => 가능
- 각 칸에서 4방향 연산 수행

# 3. 자료구조
- 전체 map : int[][]
- 로봇 청소기 위치, 방향, 전체 청소한 곳 수 : int, int int

# Tip) 
- 주어진 조건을 되도록 그대로 구현(나중에 매우 헷갈림)
- 되도록 쉽게 구현할 것
- Console에 Log 찍는 것 연습 필요
"""

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
y, x, d = map(int, input().split())

map = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

while 1 :
    if map[y][x] == 0 :
        map[y][x] = 2
        cnt += 1
        
    sw = False
    for i in range(1,5) :
        ny = y + dy[d-i]
        nx = x + dx[d-i]
        if 0<=ny<N and 0<=nx<M :
            if map[ny][nx] == 0 :
                # 그 방향으로 회전한 다음, 한 칸을 전진하고 1번부터 진행
                d = (d-i+4)%4
                y = ny
                x = nx
                sw = True
                break
            
    # 4방향 모두 있지 않은 경우
    if sw == False :
        # 바라보는 방향을 유지한 채로 뒤로 후진
        # 뒤쪽 방향이 막혀 있는지 확인
        
        ny = y - dy[d]
        nx = x - dx[d]
        if 0<=ny<N and 0<=nx<M :
            if map[ny][nx] == 1 :
                break
            else :
                y = ny
                x = nx
                
        else :
            break
        
print(cnt)
