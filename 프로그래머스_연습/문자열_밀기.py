def solution(A, B):
    answer = 0
    
    A = list(A)
    B = list(B)
    
    
    while A != B :
        temp = A[-1]
        A[1:] = A[:-1]
        A[0] = temp
        
        print(A)
        
        answer+=1
        
        if answer == len(A) :
            return -1
    
    return answer
