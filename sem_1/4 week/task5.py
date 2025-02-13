import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#считываем данные из таблицы
df = pd.read_csv('C:/Users/Эльмира/Documents/GitHub/homework/4 week/BTC_data.csv')

plt.figure(figsize=(10,10))
plt.plot(df['time'], df['close'], color="green", label="Динамика цен Bitcoin")
plt.xlabel('Время')
plt.ylabel('Цена')

plt.xticks([])
plt.yticks()

plt.grid(axis='both', linestyle='--')
plt.legend()
plt.savefig('C:/Users/Эльмира/Documents/GitHub/homework/4 week/graph_task5.png')
plt.show()
