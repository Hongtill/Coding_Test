import sys

input = sys.stdin.readline

n = int(input().strip())
count = 0

for i in range(1, n+1) :
  number_string = str(i)
  
  numbers = []
  
  for j in number_string :
    numbers.append(int(j))

  length = len(numbers)
  
  check_number = []
  
  # print(numbers)
  
  if length > 1 : 
    for k in range(0, length, 1) :
      if k+1 < length :
        check_number.append(numbers[k] - numbers[k+1])
      else :
        continue
    
    # print(numbers)
    # print(check_number)
      
    if len(set(check_number)) == 1 :
      count+=1
    else :
      pass
    
  else :
    count+=1

print(count)
