n, m = map(int, input().split())

# n : 높이
# m : 유형 1,2,3 중 하나

if ((n % 2 == 1) & (n <= 100)) & ((m>=1) & (m<=4)) :
    if m == 1 :
        for i in range(1, n//2+1):
            print('*' * i)
        for i in range(n//2+1, 0, -1):
            print('*' * i)

    elif m == 2 :
        for i in range(1, n//2+1):
            print(' ' * (n//2+1 - i), end='')
            print('*' * i)
        for i in range(n//2+1, 0, -1):
            print(' ' * (n//2+1 - i), end='')
            print('*' * i)
            
    elif m == 3 :
        for i in range(1, n//2+1):
            print(' ' * (i-1), end='')
            print('*' * (2*(n//2+1-i) + 1))
        for i in range(n//2+1, 0, -1):
            print(' ' * (i-1), end='')
            print('*' * (2*(n//2+1-i) + 1))

    elif m == 4 :
        for i in range(n//2+1, 0, -1):
            print(' ' * (n//2+1 - i), end='')
            print('*' * i)
        for i in range(n//2, 0, -1):
            print(' ' * (n//2), end='')
            print('*' * (n - n//2 - i + 1))

else :
    print('INPUT ERROR!')
