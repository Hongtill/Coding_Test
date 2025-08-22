from collections import deque

def solution(priorities, location):
    # (우선순위, 원래 위치) 튜플을 원소로 하는 큐 생성
    queue = deque([(priority, i) for i, priority in enumerate(priorities)])
    
    # 실행 순서를 기록할 변수
    count = 0

    while queue:
        # 1. 큐의 가장 앞에 있는 프로세스를 꺼냄
        current_process = queue.popleft()
        
        # 2. 현재 큐에 대기 중인 프로세스들의 우선순위 중, 가장 높은 우선순위를 찾음
        #    max 함수를 사용해 우선순위(튜플의 첫 번째 요소)만 비교
        if any(current_process[0] < other_process[0] for other_process in queue):
            # 3. 만약 더 높은 우선순위의 프로세스가 있다면,
            #    현재 프로세스를 다시 큐의 맨 뒤에 넣음
            queue.append(current_process)
        else:
            # 4. 그렇지 않다면, 현재 프로세스는 실행됨
            count += 1
            # 5. 만약 실행된 프로세스가 우리가 찾던 프로세스라면
            if current_process[1] == location:
                return count
                
    return count
