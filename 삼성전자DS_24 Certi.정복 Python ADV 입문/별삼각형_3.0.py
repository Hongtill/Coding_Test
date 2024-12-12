X = int(input())

max_num = X**2

arr = [[0 for _ in range(X)] for _ in range(X)]

x = -1
y = X-1

m = X
num = 1

while num <= max_num :
    for i in range(0, m) :
        x+=1
        arr[x][y] = num
        num+=1
        
    m-=1
        
    for i in range(0,m) :
        y-=1
        arr[x][y] = num
        num+=1
        
    for i in range(0,m) :
        x-=1
        arr[x][y] = num
        num+=1
    m-=1
    
    for i in range(0,m) :
        y+=1
        arr[x][y] = num
        num+=1
        


for i in range(X-1, -1, -1) :
    for j in range(0,X):
        print(arr[j][i], end=' ')
    print('')
        
        
