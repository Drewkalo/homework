import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

# Данные -  REPLACE THIS WITH YOUR ACTUAL T_2 DATA
r_2 = np.array([0.11, 0.12, 0.13, 0.14, 0.15, 0.16])**2
T_2 = np.array([3.37, 3.6, 3.84, 4.07, 4.31, 4.56])**2 # Example data - replace with your data


data_sets = {'T_2': T_2}

markers = ['o'] # Only one dataset, so only one marker needed
colors = ['blue']  # Only one dataset, so only one color needed

slopes = []
std_errs = []

plt.figure(figsize=(10, 8))

for i, (label, data) in enumerate(data_sets.items()):
    if len(data) > 0: # Check if data is not empty
        slope, intercept, r_value, p_value, std_err = linregress(r_2, data)
        plt.plot(r_2, data, markers[i], color=colors[i], label=label, markersize=8)
        plt.plot(r_2, slope * r_2 + intercept, '-', color=colors[i], linewidth=2, label=f'{label} (k = {slope:.6f}, погрешность = {std_err:.6f})')
        slopes.append(slope)
        std_errs.append(std_err)
    else:
        print(f"Warning: Dataset '{label}' is empty. Skipping.")

plt.xlabel('r^2, м', fontsize=12)
plt.ylabel('T^2, сек', fontsize=12)
plt.title('Зависимость T^2(r^2)', fontsize=14)
plt.legend(fontsize=10, loc='lower right')
plt.grid(True, linestyle='--')

#Robust y-axis limits handling empty data
if len(T_2) > 0:
    y_min = np.min(T_2) * 0.95
    y_max = np.max(T_2) * 1.05
    plt.ylim(y_min, y_max)
else:
    plt.ylim(0,1) # Default y-limits if data is empty


plt.savefig("graphic.png")
plt.show()

if len(slopes) > 0: #Avoid error if no slopes were calculated.
    avg_slope = np.mean(slopes)
    avg_std_err = np.mean(std_errs)
    print(f"Средний коэффициент наклона (k): {avg_slope:.6f}")
    print(f"Средняя погрешность коэффициента наклона: {avg_std_err:.6f}")
else:
    print("No data to process.")

