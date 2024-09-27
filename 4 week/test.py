import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fig = plt.figure(figsize = (16,9)) # создали рисунок/Figure Fig пропорциями 16:9
ax1 = fig.add_subplot(221) # создали Axes (подграфик) ax1 в серии из 2 графиков, поставили на позицию [1,1] -- левый верхний угол
ax2 = fig.add_subplot(222) # создали Axes ax2 в серии из 2 графиков, поставили на позицию [1,2] -- первый график во второй "строке" графиков
ax3 = fig.add_subplot(223) # создали Axes (подграфик) ax1 в серии из 2 графиков, поставили на позицию [1,1] -- левый верхний угол
ax4 = fig.add_subplot(224)

pos = 0

values1 = np.random.normal(pos, 10, 100)
values2 = np.random.normal(pos, 10, 1000)
values3 = np.random.normal(pos, 10, 10000)
values4 = np.random.normal(pos, 10, 100000)
 
ax1.hist(values1, 100)
ax2.hist(values2, 100)
ax3.hist(values3, 100)
ax4.hist(values4, 100)


plt.show()