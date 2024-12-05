import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

# Данные
M = np.array([0.066, 0.168, 0.214, 0.26, 0.405])
omega = np.array([0.0356, 0.089, 0.114, 0.137, 0.212])


# Линейная регрессия с помощью scipy.stats.linregress
slope, intercept, r_value, p_value, std_err = linregress(M, omega)

# Построение графика
plt.figure(figsize=(8, 6))
plt.plot(M, omega, 'x', label='Данные')
plt.plot(M, slope * M + intercept, '-', label=f'Линейная регрессия (k = {slope:.6f}, погрешность = {std_err:.6f})')
plt.errorbar(M, omega, xerr= M *0.00017, yerr=omega * 0.00337)

plt.xlabel('M')
plt.ylabel('Omega')
plt.title('Зависимость Omega от M')
plt.legend()
plt.grid(True, linestyle='--' )
plt.savefig("graph_1.3.5.png")
plt.show()

print(f"Коэффициент наклона (k): {slope:.6f}")
print(f"Погрешность коэффициента наклона: {std_err:.6f}")