"""
# DFS
- Stack, 재귀함수로 구현 가능
- O(V+E)

# 재귀함수 
- 자기 자신을 다시 호출하는 함수
- DFS, 백트래킹에서 중요
- 재귀함수가 종료되는 시점 반드시 명시
- 재귀함수의 깊이가 너무 깊어지면 Stack Overflow 

# 아이디어 
- 시작점에 연결된 Vertex 찾기
- 연결된 Vertex를 계속해서 찾음 (끝날 때까지)
- 더이상 연결된 Vertex 없을 경우, 다음

# 자료구조
- 검색할 그래프 : 2차원 배열
- 방문여부 확인 : 2차원 배열(재방문 금지)

# 1. 아이디어
- 2중 for문, 값 1 && 방문 X => DFS
- DFS를 통해 찾은 값을 저장 후 정렬해서 출력

# 2. 시간복잡도
- DFS : O(V+E)
- V, E : N^2, 4N^2
- V+E : 5N^2 ~= N^2 ~= 625 >> 2억 => 가능

# 3. 자료구조
- 그래프 저장 : int[][]
- 방문여부 : bool[][]
- 결과값 : int[]

"""

import sys
input = sys.stdin.readline

N = int(input())
map = [list(map(int, input().strip())) for _ in range(N)]
chk = [[False] * N for _ in range(N)]
result = []
each = 0

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def dfs(y, x) :
    global each
    each += 1 
    for k in range(4) : 
        ny = y + dy[k]
        nx = x + dx[k]
        
        if 0 <= ny < N and 0 <= nx < N :
            if map[ny][nx] == 1 and chk[ny][nx] == False :
                chk[ny][nx] = True
                dfs[ny, nx] # 재귀함수 호출

for j in range(N) :
    for i in range(N) :
        if map[j][i] == 1 and chk[j][i] == False :
            # 방문 체크 표시
            chk[j][i] = True
            each = 0
            dfs(j,i)
            result.append(each)
            # DFS로 크기 구하기
            # cf) BFS : 함수 호출, 리턴값으로 크기를 반환 받음
            # 크기를 결과 리스트에 넣기
            
result.sort()
print(len(result))

for i in result :
    print(i)
            
