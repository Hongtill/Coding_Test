import sys

input = sys.stdin.readline

n, k = map(int, input().strip().split())

coins = []

for i in range(n) :
  coin = int(input().strip())
  
  coins.append(coin)
  
coin_count = 0

for j in range(n-1, -1, -1) :
  if (k // coins[j] > 0) :
    coin_count += k // coins[j]
    
    # print(coins[j], k // coins[j])
    k = k - (coins[j] * (k // coins[j]))
    
    # print(k, coins[j])
    
    
print(coin_count)