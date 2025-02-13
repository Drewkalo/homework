a = input().split()
n = int(a[0])
l = a[1]
j = 0
k = n
res = ""

for i in range(len(l) // n):
    dop = l[j:k]                #Вспомогательный список
    res = res + dop[::-1]
    j += n
    k += n

print(res)
