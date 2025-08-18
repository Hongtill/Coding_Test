def solution(participant, completion):
    hash_dict = {}
    
    # 1. 참가자 명단을 딕셔너리에 넣고, 동명이인이 있으면 +1 해줍니다.
    for p in participant:
        # 딕셔너리에 p가 있으면 기존 값에 1을 더하고, 없으면 0을 가져온 뒤 1을 더합니다.
        hash_dict[p] = hash_dict.get(p, 0) + 1
    
    # 2. 완주자 명단을 딕셔너리에서 찾아 값을 1씩 빼줍니다.
    for c in completion:
        hash_dict[c] -= 1
        
    # 3. 딕셔너리를 확인하여 값이 0이 아닌, 즉 1인 선수가 완주하지 못한 선수입니다.
    for key, value in hash_dict.items():
        if value > 0:
            return key
