import sys

input = sys.stdin.readline

n = int(input().strip())

score_list = [list(map(int, input().split())) for _ in range(n)]

for i in range(n) :
  average_score = 0
  sum_score = 0
  count = score_list[i][0]
  over_counts = 0
  
  for j in range(1, len(score_list[i])) :
    sum_score += score_list[i][j]
  
  average_score = sum_score / count
  
  for k in range(1, len(score_list[i])) :
    if score_list[i][k] > average_score :
      over_counts += 1


  print(f"{(over_counts / count) * 100:.3f}%")
