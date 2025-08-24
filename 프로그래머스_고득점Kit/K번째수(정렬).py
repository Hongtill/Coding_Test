def solution(array, commands):
    answer = []


    for i in commands :
        temp_list = array[i[0]-1 : i[1]]
        temp_list = sorted(temp_list)
        # list.sort() 함수는 리스트를 제자리에서 정렬하고 None을 반환
        # temp_list = temp_list.sort()를 실행하면 temp_list에는 None이 할당되어 다음 코드에서 에러가 발생
        # 원본을 유지하면서 정렬된 새 리스트를 반환하는 sorted() 함수를 사용
        answer.append(temp_list[i[2]-1])

    
    return answer
