import cmath

def fft(x):
    n = len(x)
    k = n.bit_length() - 1
    for i in range(n):
        t = int(((bin(i)[2:]).rjust(k, '0'))[::-1], 2)
        if t > i:
            x[i], x[t] = x[t], x[i]
    for j in range(k):
        w0 = cmath.exp(-2j * cmath.pi / (2**(j+1)))
        for i in range(0,n,2**(j+1)):
            w = 1
            for s in range(2**j):
                x1,x2 = x[i+s],x[i+s+2**j]
                t = w*x2
                x[i+s],x[i+s+2**j] = x1 + t,x1 - t
                w = w*w0
    
    return x

def ifft(x):
    n = len(x)
    k = n.bit_length() - 1
    for i in range(n):
        t = int(((bin(i)[2:]).rjust(k, '0'))[::-1], 2)
        if t > i:
            x[i], x[t] = x[t], x[i]
    for j in range(k):
        w0 = cmath.exp(2j * cmath.pi / (2**(j+1)))
        for i in range(0,n,2**(j+1)):
            w = 1
            for s in range(2**j):
                x1,x2 = x[i+s],x[i+s+2**j]
                t = w*x2
                x[i+s],x[i+s+2**j] = x1 + t,x1 - t
                w = w*w0
    
    return [i/n for i in x] 


n = int(input())
a = input().strip()
b = input().strip()
rev_b = b[::-1]
res = [0] * len(a)
#print(alphabet)

for letter in set(a):
    vec_a = [1 if ch == letter else 0 for ch in a]
    vec_b = [1 if ch == letter else 0 for ch in rev_b]
    # print(vec_a)
    # print(vec_b)
    tmp1 = fft(vec_a)
    tmp2 = fft(vec_b)
    tmp12 = [tmp1[i] * tmp2[i] for i in range(len(tmp1))]
    tmp_all = ifft(tmp12)
    # print(tmp_all)
    for i in range(len(a)):
        res[i] += tmp_all[i].real
# print(res)
print(int(round(max(res))))