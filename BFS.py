'''
# 1. 아이디어
- 2중 for 문 => 값 1 && 방문 X => BFS
- BFS 돌면서 그림 개수 + 1, 최대값을 갱신

# 2. 시간복잡도
- BFS : O(V+3)
- V : 500 * 500
- E : 4 * 500 * 500
- V+E : 5 * 2500 = 100만 < (1초 연산 수 : 2억) => 가능!


# 3. 자료구조
- 그래프 전체 지도 : int[][]
- 방문 : bool[][]
- Queue(BFS)
'''

import sys
input = sys.stdin.readline

n, m = map(int, input())
map = [list(map(int, input().split())) for _ in range(n)]
chk = [[False] * m for _ in range(n)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def bfs(y, x) :
    rs = 1 
    q = [(y,x)]

    while q :
        ey, ex = q.pop()
        for k in range(4) :
            ny = ey + dy[k]
            nx = ex + dx[k]
            
            if 0 <= ny < n and 0 <= nx < m :
                if map[ny][nx] == 1 and chk[ny][nx] == False :
                    rs += 1
                    chk[ny][nx] = True
                    q.append((ny, nx))
        

cnt = 0
max_value = 0
# 보통 2중 for문은 y를 먼저 돌고 x를 먼저 도는 식으로 이뤄져 있음
for j in range(n) :
    for i in range(m) :
        if map[j][i] == 1 and chk[j][i] == False :
            chk[j][i] == True 
            # 전체 그림 갯수 +1
            cnt += 1
            # BFS > 그림 크기를 구해주고
            max_value = max(max_value, bfs(j,i))
            # 최대값 갱신
            
print(cnt)
print(max_value)
