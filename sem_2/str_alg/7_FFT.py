import cmath
 
a = []

#Рекурсивный fft

def fft(x):
    n = len(x)
    if n == 1:
        return x
    x_even = fft(x[::2])
    x_odd = fft(x[1::2])
    t = [cmath.exp(-2j * cmath.pi * k / n) * x_odd[k] for k in range(n // 2)]
    return [x_even[k] + t[k] for k in range(n // 2)] + [x_even[k] - t[k] for k in range(n // 2)]

#Обратный fft

def ifft(fft_x):
    n = len(fft_x)
    if n == 1:
        return fft_x
    x_even = ifft(fft_x[::2])
    x_odd = ifft(fft_x[1::2])
    t = [cmath.exp(2j * cmath.pi * k / n) * x_odd[k] for k in range(n // 2)]
    return [x_even[k] + t[k] for k in range(n // 2)] + [x_even[k] - t[k] for k in range(n // 2)]


#Перемножение полиномов

def mult_poly(p,q):
    degree = max(len(p),len(q))
    degree = 1 << ((degree-1).bit_length()+1)
    print(degree)
    new_p = [0]*degree
    new_q = [0]*degree
    new_p[:len(p)] = p
    new_q[:len(p)] = q
    fft_p = fft(new_p)
    fft_q = fft(new_q)
    fft_pq = [fft_p[i] * fft_q[i] for i in range(len(fft_p))]
    res = (np.abs(ifft(fft_pq))/degree)
    return [int(res[i]) for i in range(len(res))]