import string
a = str(input())
for i in a:
    if i in string.punctuation:
        a = a.replace(i, " ")

b = {}
words = [str(i).lower() for i in a.split()]
print(words)

for _ in words:
    if _ in b:
        b[_] += 1
    else:
        b[_] = 1

print(b)


