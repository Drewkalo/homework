a = int(input())
c = [1]
i = 1
while True:
    if i*3 < a:
        i *= 3
        c.append(i)
        continue
    if i*2 < a:
        i *= 2
        c.append(i)
        continue
    if i < a:
        i += 1
        c.append(i)
        continue
    if i == a:
        break
print(len(c)-1)
print(c)







'''while True:
    if i%2 == 0 and i%6 == 0:
        i //= 2
        c.append(i)
        continue
    if i%3 == 0:
        i //= 3
        c.append(i)
        continue
    if i-1 > 1:
        i -= 1
        c.append(i)
        continue
    if i == 1:
        break
c_ = c[::-1]
print(len(c)-1)
print(*c_, sep=" ")
'''