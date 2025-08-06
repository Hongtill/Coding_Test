# 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인


# phone_book : 전화번호를 담은 배열 
# 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false , 그렇지 않으면 true를 return
def solution(phone_book):

    hash_dict = {}
    
    for i in phone_book :
        hash_dict[i] = 1
        
    for i in phone_book :
        for _length in range(len(i)) :
            result = hash_dict.get(i[:_length], 0)
            
            if result > 0 :
                return False
        
    
    return True
