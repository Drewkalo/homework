import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = [0.03, 0.06, 0.12, 0.18, 0.24, 0.3, 0.36, 0.42]
y = [3.38, 2.41, 1.8, 1.6, 1.51, 1.52, 1.54, 1.57]

# Инициализировать рисунок/Figure
plt.figure(figsize=(8,5), dpi=100)

# Основные возможные аргументы функции plot. По умолчанию необходимы только x и y
#plt.plot(x,y, label='2x', color='red', linewidth=2, marker='.', linestyle='--', markersize=10, markeredgecolor='blue')

#нарисуем график первой функции -- 2x
plt.plot(x,y, 'b+-', color="black", markersize=10, markeredgecolor='grey')

# Добавим заголовок (в fontdict нужен словарь, шрифт должен поддерживаться matplotlib'ом)
plt.title('Зависимость периода колебаний от a', fontdict={'fontname': 'sans-serif', 'fontsize': 20})

# Подпишем оси
plt.ylabel('Период колебаний T, сек')
plt.xlabel('Расстояние от Ц.М до оси, м')

# Зададим какие-нибудь корявые "штрихи"/ticks на осях. в эти фунции можно передать любой список
plt.xticks()
plt.yticks()

plt.grid()

# функция легенды графика для отображения label'ов графиков
plt.legend()

# Можем сохранить график в высоком качестве
plt.savefig('graph.png', dpi=300)

# И вызвать эту функцию чтобы график сразу после отрисовки не пропал, пока мы его не закроем
plt.show()