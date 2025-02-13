import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = [0.03, 0.06, 0.12, 0.18, 0.24, 0.3, 0.36, 0.42]
y = [3.38, 2.41, 1.8, 1.6, 1.51, 1.52, 1.54, 1.57]

plt.figure(figsize=(8,5), dpi=100)

plt.plot(x,y, 'b+-', color="black", markersize=10, markeredgecolor='grey')

plt.title('Зависимость периода колебаний от a', fontdict={'fontname': 'sans-serif', 'fontsize': 20})

plt.ylabel('Период колебаний T, сек')
plt.xlabel('Расстояние от Ц.М до оси, м')

plt.xticks()
plt.yticks()

plt.grid()

plt.legend()

plt.savefig('graph.png', dpi=300)

plt.show()