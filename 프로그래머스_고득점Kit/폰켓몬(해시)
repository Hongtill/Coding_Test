# 총 N 마리의 폰켓몬 중에서 N/2마리를 가져가도 좋다

# 폰켓몬은 종류에 따라 번호를 붙여 구분
# 같은 종류의 폰켓몬은 같은 번호
# 최대한 많은 종류의 폰켓몬을 포함해서 N/2마리를 선택

# nums는 폰켓몬의 종류 번호가 담긴 1차원 배열
# nums의 길이(N) : 항상 짝수
def solution(nums):
    answer = 0
    
    hash_dict = {}
    
    for ponketmon_num in nums :
        hash_dict[ponketmon_num] = hash_dict.get(ponketmon_num, 0) + 1
        
    if len(hash_dict) > len(nums)/2 :
        answer = len(nums)/2
    else :
        answer = len(hash_dict)
    
    return answer
