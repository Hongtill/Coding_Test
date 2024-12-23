n = int(input())

# n : 사각형 변 길이

arr = [[0 for _ in range(n)] for _ in range(n)]

num = 1

# for i in range(0, n) :
#     for j in range(0, n) :
#         arr[i][j] = 1
        


way = 0
count = 1
max_count = n**2
max_len = 1

x = 0
y = n-1
arr[x][y] = 1
# for i in range(n-1, -1,) :
#     for j in range(0, n) :
#         print(arr[j][i], end='')
#     print(' ')
# print('===')
#==================================================
while max_len < n :
    max_len = 1
    
    if (way == 0) & (y-1 >= 0) :
        y -= 1
        
        count += 1
        arr[x][y] = count
        
        way = 1
        
    elif way == 1 :
        while (x+1 < n) and (y+1 < n) :
            x += 1
            y += 1
            count += 1
            max_len += 1
            
#             print(x,y)
            
            arr[x][y] = count
            
        way = 2 
    
        
    elif (way == 2) and (x+1 < n):
        
        x += 1 
        
        count += 1
        arr[x][y] = count
        
        way = 3
        
    elif way == 3 :
        while (x-1>=0) and (y-1>=0) :
            x -= 1
            y -= 1
            count += 1
            max_len += 1
            
            arr[x][y] = count
            
        way = 0
        
#     print(way)
#     for i in range(n-1, -1, -1) :
#         for j in range(0, n) :
#             print(arr[j][i], end=' ')
#         print('')
#     print('===')
#     print('max_len : ', max_len)
        
#==================================================
if way == 2 : #오른쪽 위로 상승하고 phase 1 마무리한 경우
    way_2 = 0
    
elif way == 0 : #왼쪽 아래로 하강하고 phase 1 마무리한 경우
    way_2 = 2
#==================================================
while count < max_count :
    if way_2 == 0 :
        y -= 1
        
        count += 1
        arr[x][y] = count
        
        way_2 = 1
        
    elif way_2 == 1 :
        while (x-1>=0) and (y-1>=0) :
            x -= 1
            y -= 1

            count += 1
            arr[x][y] = count
        
        way_2 = 2
        
    elif way_2 == 2 :
        x += 1
        
        count += 1
        arr[x][y] = count
        
        way_2 = 3
        
    elif way_2 == 3 :
        while (x+1<n) and (y+1<n) :
            x += 1
            y += 1

            count += 1
            arr[x][y] = count
        
        way_2 = 0
        
#     print(way)
#     for i in range(n-1, -1, -1) :
#         for j in range(0, n) :
#             print(arr[j][i], end=' ')
#         print('')
#     print('===')
        
        
# 출력 코드
for i in range(n-1, -1, -1) :
    for j in range(0, n) :
        print(arr[j][i], end=' ')
    print('')
   
