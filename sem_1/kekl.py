import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Входные данные (давление в торрах и D)
pressure_torr = np.array([52.22, 59.68, 74.6, 96.98])
D = np.array([3.550551, 2.878412, 2.866282, 2.282592])

# Пересчет давления в обратные торры (1/торр)
pressure_inv_torr = (1 / pressure_torr) * 10**3

# Линейная регрессия (метод наименьших квадратов)
slope, intercept, r_value, p_value, std_err = stats.linregress(pressure_inv_torr, D)

# Вывод коэффициентов
print("Коэффициенты линейной регрессии:")
print("Наклон (slope):", slope)
print("Пересечение (intercept):", intercept)
print("Коэффициент детерминации (R-квадрат):", r_value**2)

# Создание точек для линии регрессии для графика
x_reg = np.linspace(0, max(pressure_inv_torr) * 1.1, 100)  # Немного увеличиваем область по оси X для наглядности
y_reg = slope * x_reg + intercept


# Экстраполяция до атмосферного давления
atmospheric_pressure_torr = 760
atmospheric_pressure_inv_torr = 1 / atmospheric_pressure_torr*10**3
D_at_atmospheric = slope * atmospheric_pressure_inv_torr + intercept

# Оценка погрешности экстраполяции (упрощенная)
#  Предполагаем, что основная погрешность обусловлена погрешностью наклона
D_at_atmospheric_error = std_err * atmospheric_pressure_inv_torr

print("\nЭкстраполяция до атмосферного давления:")
print("D при атмосферном давлении (торр^-1):", D_at_atmospheric)
print("Погрешность D при экстраполяции (торр^-1):", D_at_atmospheric_error)


# Построение графика
plt.figure(figsize=(8, 6))
plt.scatter(pressure_inv_torr, D, label='Данные', marker='o')
plt.plot(x_reg, y_reg, color='red', label=f'Линейная регрессия (y = {slope:.2f}x + {intercept:.2f})')
plt.xlabel('1/P (торр$^{-1}$ * $10^{3}$)')
plt.ylabel('D')
plt.title('Зависимость D от 1/P')

# Отмечаем точку экстраполяции
plt.scatter(atmospheric_pressure_inv_torr, D_at_atmospheric, color='green', marker='x', s=100, label=f'Экстраполяция при 1 атм (D={D_at_atmospheric:.3f} ± {D_at_atmospheric_error:.3f})')
plt.scatter((1/(37.3))*10**3,6.70505, color='blue', marker='o')

plt.legend()
plt.grid(True)
plt.show()
