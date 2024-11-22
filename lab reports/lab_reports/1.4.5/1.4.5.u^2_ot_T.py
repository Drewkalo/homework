import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

# Данные
T = np.array([11, 15.9, 19.28, 24.23, 29.18])
u2 = np.array([141.79, 167.37, 184.41, 205.99, 225.13])**2


# Линейная регрессия с помощью scipy.stats.linregress
slope, intercept, r_value, p_value, std_err = linregress(T, u2)

# Построение графика
plt.figure(figsize=(8, 6))
plt.plot(T, u2, 'x', label='Данные')
plt.plot(T, slope * T + intercept, '-', label=f'Линейная регрессия (k = {slope:.2f}, погрешность = {std_err:.2f})')

plt.xlabel('T')
plt.ylabel('u^2')
plt.title('Зависимость u^2 от T')
plt.legend()
plt.grid(True)
plt.show()

print(f"Коэффициент наклона (k): {slope:.2f}")
print(f"Погрешность коэффициента наклона: {std_err:.2f}")