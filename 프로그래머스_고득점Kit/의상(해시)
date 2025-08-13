# 각 종류별로 최대 1가지 의상만 착용
# 코니는 하루에 최소 한 개의 의상은 입습니다.

def solution(clothes):
    
    closet = {}
    
    for cloth in clothes :
        category = cloth[1]
        closet[category] = closet.get(category, 0) + 1
        
    answer = 1
    for kind in closet:
        answer *= (closet[kind] + 1)
        
    # 3. 아무것도 입지 않은 경우(1가지)를 제외
    return answer - 1
        
        
