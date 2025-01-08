"""
# 백트래킹
- 모든 경우의 수를 확인해야 할 때
- for 문으로는 확인이 불가한 경우 (for이 돌 때마다 깊이가 달라질 때)
- ex) 순열

# 아이디어
- 1부터 N 중에 하나를 선택한 뒤
- 다음 1부터 N까지 선택할 때, 이미 선택한 값이 아닌 경우를 선택
- M개를 선택한 경우, print

# 시간복잡도
- N^N : 중복 가능, N=8까지 가능 (2억 미만)
- N! : 중복 불가, N=10까지 가능 (2억 미만)

# 자료구조
- 방문 여부 확인 배열 : bool[]
- 선택한 값 입력 배열 : int[]

# Tip)
- 백트래킹 문제는 N이 작음 (10이하)
- 재귀함수 사용 할 때, 종료시점 잊지 말기!

# 1. 아이디어
- 백트래킹 재귀함수 안에서 for 돌면서 숫자 선택 (이때 방문여부 확인)
- 재귀함수에서 M개를 선택할 경우 print

# 2. 시간복잡도
- N! (N은 최대 8) => 가능

# 3. 자료구조
- 방문 여부 체크 : bool[]
- 결과값 저장 : int[]


"""


import sys
input = sys.stdin.readline

N, M = map(int, input().split())
rs = []
chk = [False] * (N+1)

def recur(num) :
    if num == M :
        print(' '.join(map(str,rs)))
        return 
    for i in range(1, N+1) :
        if chk[i] == False :
            chk[i] = True
            rs.append(i)
            recur(num+1)
            chk[i] = False
            rs.pop()
            
            
recur(0)
