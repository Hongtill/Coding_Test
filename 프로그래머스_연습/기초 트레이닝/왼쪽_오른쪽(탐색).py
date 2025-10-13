def solution(str_list):
    
    
    for i, character in enumerate(str_list) :
        
        character_map = {character: i for i, character in enumerate(str_list)}
        
        if 'l' not in character_map.keys() :
            if 'r' not in character_map.keys() :
                final_answer = []
                break

        if character == 'l' :
            final_answer = str_list[:i]
            break

        elif character == 'r' :
            final_answer = str_list[i+1:]
            break
            

    
    return final_answer
