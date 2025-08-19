def solution(s):
    answer = True
    
    check = []
    
    for i in range(len(s)) :
        if len(check) == 0 :
            if s[i] == '(' :
                check.append(s[i])
            else :
                answer = False
                break
        else :
            if s[i] == ')' :
                if check.pop() == '(' :
                    answer = True
                else :
                    answer = False
                    break
            else :
                check.append(s[i])

                
    if len(check) > 0 :
        answer = False
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.

    return answer
