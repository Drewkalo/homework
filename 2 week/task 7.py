a = [c for c in input().strip()]
max = 0
d = ''
for j in a:
    if a.count(j) >= max and j != " ":
        max = a.count(j)
        d = j

print(d)