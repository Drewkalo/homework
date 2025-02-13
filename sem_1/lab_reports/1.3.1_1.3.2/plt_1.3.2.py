import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

# Данные (same as before)
# Данные
M = np.array([0, 0.049, 0.099, 0.149, 0.199, 0.249, 0.348, 0.448])
n1_asc = np.array([0, 0.022, 0.042, 0.06, 0.091, 0.107, 0.143, 0.19])/1.42
n1_des = np.array([0, 0.026, 0.042, 0.06, 0.082, 0.109, 0.153, 0.19])/1.42
n2_asc = np.array([0, 0.026, 0.041, 0.061, 0.085, 0.099, 0.146, 0.189])/1.42
n2_des = np.array([0, 0.025, 0.044, 0.065, 0.086, 0.108, 0.146, 0.189])/1.42
n3_asc = np.array([0, 0.025, 0.041, 0.063, 0.085, 0.108, 0.138, 0.182])/1.42
n3_des = np.array([0, 0.022, 0.039, 0.06, 0.081, 0.1, 0.149, 0.182])/1.42
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
    slope, intercept, r_value, p_value, std_err = linregress(M, data)
    plt.plot(M, data, markers[i], color=colors[i], label=label)  #Added color
    plt.plot(M, slope * M + intercept, '-', color=colors[i], label=f'{label} (k = {slope:.6f}, погрешность = {std_err:.6f})')
    slopes.append(slope)
    std_errs.append(std_err)

plt.xlabel('M, н*м', fontsize=12)
plt.ylabel('phi, grad', fontsize=12)
plt.title('Зависимость M(phi)', fontsize=14)
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
