import matplotlib.pyplot as plt
#from sklearn.linear_model import LinearRegression
from scipy.optimize import curve_fit
import numpy as np
import matplotlib as mpl
from math import *

def mapping(x, k, b):
    return  k * x + b

#plt.figure(figsize=(10,10), dpi=100)
#plt.title(r"Зависимость периода колебаний от положения груза")
#plt.xlabel("u = T^2*xц, с^2*м")
#plt.ylabel("v = a^2, м^2")
l = 1
a = np.array([0.42, 0.36, 0.3, 0.24, 0.18, 0.12, 0.06, 0.03])
N = len(a) # число точек
n = np.array([40, 40, 40, 40, 40, 40, 40, 40])
t = np.array([62.8, 61.5, 60.7, 60.58, 63.9, 72, 96.5, 135.1])
t_per = np.array(t) / n
sigma_t = 0.137
sigma_a = 0.5e-3
sigma_T = sigma_t / t * t_per
gs = 4 * np.pi**2 * ( l**2 / 12 + a**2 ) / (a * t_per**2)
gm = np.mean(gs)
print(gs)
print("g_mean = %.3f" % gm)

sigma_gm = np.std(gs) / np.sqrt(N)
print("sigma_gm = %.3f" % sigma_gm)

u = t_per**2 * a
v = a**2
sigma_u = u * np.sqrt(4 * (sigma_T / t_per)**2 + (sigma_a/a)**2)
sigma_v = 2 * a * sigma_a
print(sigma_u/u, '\n', sigma_v/v)
mu = np.mean(u) # средее
mv = np.mean(v)
mv2 = np.mean(v**2) # средний квадрат
mu2 = np.mean(u**2)
muv = np.mean (u * v) # среднее от произведения
k = (muv - mu * mv) / (mv2 - mv**2)
b = mu - k * mv
print("k = ", k, ", b = ", b)

plt.figure(figsize=(8,6), dpi=100) # размер графика
plt.ylabel("$u=T^2 a$, $с^2 \cdot м$") # подписи к осям
plt.xlabel("$v=a^2$, $м^2$")
plt.title('Наилучшая прямая для линеаризованной зависимости $T(a)$') # заголовок␣
plt.grid(True, linestyle="--") # сетка
plt.axis([0,0.25,0,1.3]) # масштабы осей
x = np.array([0., 1]) # две точки аппроксимирующей прямой
plt.plot(x, k * x + b, "-r",linewidth=1, label="Линейная аппроксимация $u = %.2f v + %.2f$"% (k, b)) # аппроксимация
plt.errorbar(v, u, xerr=sigma_a, yerr=sigma_T, fmt="ok", label="Экспериментальные точки", ms=3) # точки с погрешностями
plt.legend() # леген
#plt.savefig("mnkgraph.png", dpi=300)
#plt.show()
g = (4 * np.pi**2) / k
print("g = %.3f" % g)

L = (3 * b * g) / np.pi**2
print("L = %.3f м" % L)

N = len(v) # число точек
sigma_k = np.sqrt(1/(N-2) * ( (mu2 - mu**2)/(mv2 - mv**2) - k**2 ) )
sigma_b = sigma_k * np.sqrt(mv2)
sigma_g = sigma_k / k * g
sigma_L = L * np.sqrt( (sigma_b / b)**2 + (sigma_g / g)**2 )
print("sigma_k = %.3f, sigma_b = %.3f" % (sigma_k, sigma_b))
print("sigma_g = %.3f, sigma_L = %.3f" % (sigma_g, sigma_L))

#sigma_u = u * np.sqrt(4 * (sigma_T / t_per)**2 + (sigma_a/a)**2)
#sigma_v = 2 * a * sigma_a

'''print(x)
print(y)

k = 0
b = 0
coeffs,_ = curve_fit(mapping, x, y)
k, b = coeffs
y_fit = []
for i in range(len(x)):
  y_fit.append(k * x[i] + b)
print(k, b)
plt.plot(x, y, '+', label='u(v)')
plt.plot(x, y_fit, label="Аппроксимирующая прямая y = kx + b, k = 3.767, b = 0.3 ")

plt.grid(visible = True, which='major', axis='both', alpha=1)
plt.grid(visible = True, which='minor', axis='both', alpha=1)

print(0.00041*((sum([float(v)*2 for v in x])/len(x))**0.5))

plt.legend()
plt.savefig('mnkgr.png', dpi=300)
plt.show() 
'''
