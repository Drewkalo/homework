import cmath
 
a = []
b = []
deg_a = len(a)
deg_b = len(b)

if (deg_a - 1).bit_length() != 


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

    t = [cmath.exp(-2j * cmath.pi * k / deg) * temp2(k)  for k in range(deg//2)]
    return [(temp1[k] + t[k]) for k in range(deg//2)] + [(temp1[k] - t[k]) for k in range(deg//2)]


fft_a = FFT(a, len(a))
fft_b = FFT(b, len(b))

fft_ab = [fft_a[k] * fft_b[k] for k in len(fft_a)]

polynom = iFFT(fft_ab, len(fft_ab))