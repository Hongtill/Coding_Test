N, M = map(int, input().split())

# N : 삼각형 높이 = 밑변의 길이
# M : 삼각형 유형 (1,2,3 중 하나)

arr = [[-1 for _ in range(N)] for _ in range(N)]

for i in range(0, N):
    num = N - i
    for j in range(0, num) :
        arr[i][j] = 1


for i in range(N-1, -1, -1) : #행 (y)
    for j in range(0,N) : #열 (x)
        left_upper = 0
        right_upper = 0
        
        if (j-1 >= 0) and (i+1 < N) :
            if arr[j-1][i+1] >= 1 :
                left_upper = arr[j-1][i+1]
                
        if (left_upper >= 1) and (i+1 < N) :
            if arr[j][i+1] >= 1 :
                right_upper = arr[j][i+1]
        
        if (left_upper >= 1) and (right_upper >= 1) :
            arr[j][i] = left_upper + right_upper

if M == 1 :
    for i in range(N-1, -1, -1) :
        for j in range(0, N) :
            if arr[j][i] > 0 :
                print(arr[j][i], end=' ')
        print('')
        
if M == 2 :
    for i in range(0, N) :
        print(' '*i, end='')
        for j in range(0, N) :
            if arr[j][i] > 0 :
                print(arr[j][i], end=' ')
        print('')

if M == 3 :
    
    arr_2 = [[-1 for _ in range(N)] for _ in range(N)]
    
    for i in range(0, N) :
        for j in range(0, N) :
            if arr[j][i] > 0 :
                arr_2[i][j] = arr[j][i]
                
    for i in range(N-1, -1, -1) :
        for j in range(0, N) :
            if arr_2[j][i] > 0 :
                print(arr_2[j][i], end=' ')
        print('')


# for i in range(N-1, -1, -1) :
#     for j in range(0, N) :

#         print(arr[j][i], end=' ')
#     print('')
