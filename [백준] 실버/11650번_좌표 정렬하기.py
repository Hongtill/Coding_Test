import sys

N = int(input())
dot_list = []

for _ in range(N):
  dot = list(map(int, sys.stdin.readline().split()))
  dot_list.append(dot)

# print(dot_list)
dot_list.sort(key=lambda x: (x[0], x[1]))

for j in range(N):
  print(dot_list[j][0], dot_list[j][1])
