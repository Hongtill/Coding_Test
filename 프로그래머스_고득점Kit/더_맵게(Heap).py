# 모든 음식의 스코빌 지수를 K 이상
# 스코빌 지수가 가장 낮은 두 개의 음식을 아래와 같이 특별한 방법 : 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
# 모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복하여 섞습니다.

# answer : 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수 (모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return)

# Heap(힙) : 최대값이나 최솟값을 빠르게 찾아내도록 만들어진 자료구조 (완전 이진 트리의 일종으로 우선순위 큐를 위하여 만들어진 자료구조)

import heapq
from heapq import heappush, heappop
from heapq import heapify

def solution(scoville, K):
    answer = 0
    
    heapify(scoville)
    
    while (len(scoville) >= 2) :
        
            
        first_scoville = heapq.heappop(scoville)
        
        if first_scoville >= K :
            return answer
            
            
        second_scoville = heapq.heappop(scoville)
        result_scoville = first_scoville + (second_scoville * 2)

        heapq.heappush(scoville, result_scoville)
        
        answer += 1

        
    if scoville[0] < K :
        return -1
    else :
        return answer
        
