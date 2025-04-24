import cmath
 
a = []

def FFT(a, deg):
    if len(a) == 1:
        return a[0]
    
    even = a[::2]
    odd = a[1::2]
    
    temp1 = FFT(even, deg/2)
    temp2 = FFT(odd, deg/2)

    t = [cmath.exp(2j * cmath.pi * k / deg) * temp2(k)  for k in range(deg//2)]
    return [(temp1[k] + t[k]) for k in range(deg//2)] + [(temp1[k] - t[k]) for k in range(deg//2)]

def iFFT(a, deg):
    if len(a) == 1:
        return a[0]
    
    even = a[::2]
    odd = a[1::2]
    
    temp1 = iFFT(even, deg/2)
    temp2 = iFFT(odd, deg/2)

    t = [cmath.exp(2j * cmath.pi * k / deg) * temp2(k)  for k in range(deg//2)]
    return [(temp1[k] + t[k]) for k in range(deg//2)] + [(temp1[k] - t[k]) for k in range(deg//2)]
