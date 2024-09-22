s = 1
a = list(map(int, input().split()))

for i in a:
    s *= i

print(s ** (1/len(a)))