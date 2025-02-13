import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#считываем данные из таблицы
df = pd.read_csv('C:/Users/Эльмира/Documents/GitHub/homework/4 week/iris_data.csv')

#переменные
pool = ["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"]

#распишем все возможные комбинации графиков, исключая повторения и зависимости типа: 'а от а'
combinations = [('SepalLengthCm', 'SepalWidthCm'), ('SepalLengthCm', 'PetalLengthCm'), ('SepalLengthCm', 'PetalWidthCm'), ('SepalWidthCm', 'PetalLengthCm'), ('SepalWidthCm', 'PetalWidthCm'), ('PetalLengthCm', 'PetalWidthCm')]


for x, y in combinations:
  print(x,y)
  
  #создаём  окно графиков
  plt.figure(figsize=(10, 10))

  #scatter расставляет точки значений с координатами, взятыми из переданных ему массивов
  plt.scatter(df[x], df[y], marker="1", color='r', label='Данные CSV')

  #считаем коэффициенты МНК
  coeffs = np.polyfit(df[x], df[y], 1)

  #линейный многочлен с коэффициентами мнк(чтобы изобразить прямую), подсмотрено на хабре
  poly_eq = np.poly1d(coeffs)
  
  #строим прямую
  plt.plot(df[x], poly_eq(df[x]), color='black', label='Прямая МНК')
  plt.xlabel(x)
  plt.ylabel(y)
  plt.title(f'{x} от {y}')
  plt.legend()
  plt.grid(axis='both', linestyle='--')
  plt.savefig(f'C:/Users/Эльмира/Documents/GitHub/homework/4 week/task4_graphs/{x}_vs_{y}.png')
  plt.close()