def step(n):
 if n == 1:
  return 0
 p = [9*(10**10)] * (n + 1)
 p[1] = 0
 for i in range(2, n + 1):
  p[i] = min(p[i], p[i - 1] + 1) # Добавление 1
  if i % 2 == 0:
   p[i] = min(p[i], p[i // 2] + 1) # Удвоение
  if i % 3 == 0:
   p[i] = min(p[i], p[i // 3] + 1) # Утроение
 return p[n]

n = int(input())
print(step(n))