f = open('C:/Users/Эльмира/Documents/GitHub/homework/1 week/formst.txt')
num1 = f.readline().strip()
op = f.readline().strip()
dig = [int(num) for num in num1.split()]

if op == '+':
    s = sum(dig)
elif op == '-':
    s = dig[0] - sum(dig[1:])
elif op == '*':
    s = 1
    for i in dig:
        s *= i

print(s)
f.close()
z = open('C:/Users/Эльмира/Documents/GitHub/homework/1 week/output.txt', 'w')
z.write(str(s))
z.close()