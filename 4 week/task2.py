import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fig = plt.figure(figsize = (16,9))
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)

pos = 10

values1 = np.random.normal(pos, 10, 100)
values2 = np.random.normal(pos, 10, 1000)
values3 = np.random.normal(pos, 10, 10000)
values4 = np.random.normal(pos, 10, 100000)
 
ax1.hist(values1, 100)
ax2.hist(values2, 100)
ax3.hist(values3, 100)
ax4.hist(values4, 100)

plt.savefig('C:/Users/Эльмира/Documents/GitHub/homework/4 week/graph_task2.png')

plt.show()