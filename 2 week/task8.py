n = int(input())
c = [int(c) for c in input() if c != ' ']
for i in range(n//2):
    del c[c.index(max(c))]
    del c[c.index(min(c))]

print(c)