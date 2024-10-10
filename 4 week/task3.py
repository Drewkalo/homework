import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('C:/Users/Эльмира/Documents/GitHub/homework/4 week/iris_data.csv')

fig = plt.figure(figsize = (16,9))
a1 = fig.add_subplot(121)
a2 = fig.add_subplot(122)

les12 = [c for c in df['PetalLengthCm'] if c <= 1.2]
more12 = [j for j in df['PetalLengthCm'] if j > 1.2]

les15 = [c for c in df['PetalLengthCm'] if c <= 1.5]
more15 = [c for c in df['PetalLengthCm'] if c > 1.5]

a1.pie([len(les12), len(more12)], labels = ['<= 1.2 cm','> 1.2 cm,'])
a2.pie([len(les15), len(more15)], labels = ['<= 1.5 cm','> 1.5 cm,'])

plt.savefig('C:/Users/Эльмира/Documents/GitHub/homework/4 week/graph_task3.png')

plt.show()