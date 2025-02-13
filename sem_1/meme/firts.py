n = int(input())
s = list(map(int, input().split()))
new = [0,0,0]
sp = sum(s)
ss = sum(s)//3
if sum(s)%3 != 0:
  pass
else:
  for i in range(3):
    new[i] = max(s)
    del s[s.index(max(s))]
  for i in range(3):
    if new[i] > ss:
      break
  while s != []:
    for _ in range(3):
      try:
        if new[_] == ss:
          continue
        if new[_] < ss:
          new[_] += min(s)
          del s[s.index(min(s))]
      except:
        break
if (new[0] == new[1] == new[2] and new[0] != 0) or (sum(new) == sp and n > 3):
  print(1)
else:
  print(0)