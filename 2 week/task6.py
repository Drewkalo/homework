a = [c for c in input()]
otv = ''

for j in a:
    if a.count(j) == 1:
        otv += j
        otv += " "

print(otv)