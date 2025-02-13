def step(m, n):
  if m < 1 or n < 1:  
    return 0
  if m == 1 and n == 1:
    return 1
  cnt = step(m - 1, n - 2) + step(m - 2, n - 1)
  return cnt

i = list(map(int,input().split()))
print(step(i[0], i[1]))