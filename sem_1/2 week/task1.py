a = list(map(int, input().split()))
count = a[0]
a_r = a[1:]
dig = 0

for j in range(count + 1):
    dig = dig ^ j
for j in a_r:
    dig = dig ^ j

print(dig)
