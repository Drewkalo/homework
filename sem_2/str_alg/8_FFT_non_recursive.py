import cmath
import string
a = [0,1,2,3,4,5,6,7]


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

print(ifft(fft([0,1,2,3,4,5,6,7])))

