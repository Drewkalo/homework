import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

# Данные (same as before)
# Данные
F = np.array([2.455, 4.913, 7.368, 9.824, 12.285, 14.742, 17.198, 19.659, 22.111, 24.568])
n1_asc = np.array([26.2, 27.3, 28.7, 30, 31.3, 32.6, 34, 35.4, 36.6, 37.8])/100
n1_des = np.array([26.4, 27.8, 29.2, 30.3, 31.4, 32.9, 34, 35.3, 36.6, 37.8])/100
n2_asc = np.array([26.4, 27.8, 29.2, 30.3, 31.7, 33, 34.2, 35.4, 36.6, 37.9])/100
n2_des = np.array([26.8, 28.1, 29.4, 30.5, 31.8, 33, 34.2, 35.4, 36.7, 37.9])/100
n3_asc = np.array([26.8, 28.1, 29.4, 30.6, 32, 33.2, 34.5, 35.6, 36.8, 38])/100
n3_des = np.array([26.8, 28.1, 29.2, 30.6, 31.7, 33.2, 34.5, 35.7, 36.8, 38])/100
data_sets = {
    'n1_asc': n1_asc,
    'n1_des': n1_des,
    'n2_asc': n2_asc,
    'n2_des': n2_des,
    'n3_asc': n3_asc,
    'n3_des': n3_des,
}

markers = ['o', 'x', '+', '|', 's', 'D']
colors = ['blue', 'green', 'red', 'purple', 'orange', 'brown'] # Different colors
slopes = []
std_errs = []

plt.figure(figsize=(10, 8)) # Increased figure size

for i, (label, data) in enumerate(data_sets.items()):
    slope, intercept, r_value, p_value, std_err = linregress(F, data)
    plt.plot(F, data, markers[i], color=colors[i], label=label)  #Added color
    plt.plot(F, slope * F + intercept, '-', color=colors[i], label=f'{label} (k = {slope:.6f}, погрешность = {std_err:.6f})')
    slopes.append(slope)
    std_errs.append(std_err)

plt.xlabel('F, н', fontsize=12)
plt.ylabel('n, см', fontsize=12)
plt.title('Зависимость n(F)', fontsize=14)
plt.legend(fontsize=10, loc='lower right')  # Increased legend font size
plt.grid(True, linestyle='--')

# Adjust y-axis limits for better visualization
plt.ylim(min(np.min(n1_asc), np.min(n1_des), np.min(n2_asc), np.min(n2_des), np.min(n3_asc), np.min(n3_des)) * 0.98,
         max(np.max(n1_asc), np.max(n1_des), np.max(n2_asc), np.max(n2_des), np.max(n3_asc), np.max(n3_des)) * 1.02)
plt.savefig("graphic.png")
plt.show()

avg_slope = np.mean(slopes)
avg_std_err = np.mean(std_errs)

print(f"Средний коэффициент наклона (k): {avg_slope:.6f}")
print(f"Средняя погрешность коэффициента наклона: {avg_std_err:.6f}")

