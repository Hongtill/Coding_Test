# 문제점: list.index() 메소드는 리스트를 처음부터 끝까지 순차적으로 탐색합니다. players의 길이가 N일 때, 이 연산의 시간 복잡도는 평균적으로 O(N)입니다. callings의 길이가 M이라면, 총 시간 복잡도는 O(M * N) 이 됩니다.
# 최악의 경우 1,000,000 * 50,000 = 500억 번의 연산이 필요하므로, 이는 명백한 시간 초과를 유발합니다.

# 시간 초과의 원인은 '선수의 현재 위치를 찾는 데 시간이 오래 걸린다'는 점입니다. 이 탐색 시간을 O(1)로 줄일 수 있다면 문제를 해결할 수 있습니다. 
# 이럴 때 가장 적합한 자료구조가 바로 딕셔너리(Dictionary) 또는 해시맵(Hash Map)

def solution(players, callings):
    
    """
    선수들의 이름과 해설진이 부른 이름을 바탕으로 최종 등수를 계산하는 함수.

    Args:
        players: 1등부터 현재 등수 순서대로 담긴 선수 이름 배열.
        callings: 해설진이 부른 이름이 담긴 배열.

    Returns:
        경주가 끝났을 때 선수들의 최종 등수 순서 배열.
    """
    
    # 선수 이름과 현재 등수(인덱스)를 매핑하는 딕셔너리 생성
    # 시간 복잡도: O(N), N은 players의 길이
    player_map = {player: i for i, player in enumerate(players)}
    
    # callings를 순회하며 등수 변경 처리
    # 시간 복잡도: O(M), M은 callings의 길이
    for called_player in callings:
        # 1. 호출된 선수의 현재 등수(인덱스)를 O(1)로 조회
        current_rank = player_map[called_player]
        
        # 2. 추월당할 선수(바로 앞 선수)의 이름 확인
        player_to_overtake = players[current_rank - 1]
        
        # 3. players 리스트에서 두 선수의 위치를 교환(swap)
        players[current_rank - 1], players[current_rank] = players[current_rank], players[current_rank - 1]
        
        # 4. 딕셔너리에 변경된 등수(인덱스) 정보를 업데이트
        player_map[called_player] = current_rank - 1
        player_map[player_to_overtake] = current_rank
        
    return players
