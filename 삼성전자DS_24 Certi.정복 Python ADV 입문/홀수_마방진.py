n = int(input())

max_num = n**2

arr = [[0 for _ in range(n)] for _ in range(n)]

# print(arr)

# 첫 번째 숫자인 1을 넣는 위치 : 첫 번째 행 가운데
arr[n//2][n-1] = 1

x = n//2
y = n
num = 1
while num < max_num :
    num += 1
    
    if (num%n == 1) :
        if (y-1 >= 0):
            y -= 1
            arr[x][y] = num
        else :
            x -= 1
            y = 0
            arr[x][y] = num
            
    else :
        if (y+1 <= n-1) & (x-1 >= 0) :
            x -= 1
            y += 1

            arr[x][y] = num
            
        elif (y+1 > n-1) :
            x -= 1
            y = 0
            arr[x][y] = num
            
        elif (x-1 < 0) :
            x = n-1
            y += 1
            arr[x][y] = num
            
#     print('x:', x)
#     print('y:', y)
#     print(num)
            
    # 출력 코드
for i in range(n-1, -1, -1) :
    for j in range(0, n) :
        print(arr[j][i], end=' ')
    print('')
#     print('========')
   
