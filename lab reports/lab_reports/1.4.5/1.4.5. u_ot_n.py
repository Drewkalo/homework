import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import linregress

# Данные
data = {
  'T1': ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [137.9, 278.3, 416.7, 557.4, 696.75, 841.6, 979.18, 1126.2, 1267.8, 1417]),
  'T2': ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [165, 331, 497, 662, 829.7, 996, 1164.4, 1333, 1501, 1673]),
  'T3': ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [182, 365, 549, 731, 916, 1099, 1284, 1469, 1656, 1843]),
  'T4': ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [204, 409, 614, 818, 1024, 1229, 1436, 1642, 1851, 2059]),
  'T5': ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [223, 447, 671, 895, 1120, 1344, 1571, 1795, 2023, 2250]),
}

# Построение графика
plt.figure(figsize=(10, 6)) # Увеличим размер графика для лучшей читаемости

for group, (n, Vn) in data.items():
  slope, intercept, r_value, p_value, std_err = linregress(n, Vn)
  line = slope * np.array(n) + intercept
  plt.plot(n, Vn, 'x', label=f'{group} (R^2 = {r_value**2:.2f})')
  plt.plot(n, line, '-', label=f'{group} - Линейная регрессия')


plt.xlabel('Номер гармоники (n)')
plt.ylabel('Частота (Vn)')
plt.title('Зависимость частоты от номера гармоники')
plt.legend()
plt.grid(True)
plt.show()
