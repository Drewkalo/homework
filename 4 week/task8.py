a = [1,2,3,4,5]
b = [4,5,6,7,8]
print(f'Уникальные для A:{set(a).difference(set(b))} \nУникальные для B:{set(b).difference(set(a))}') #уникальные для каждого списка
print(set(a+b)) #уникальные для объединения списков
print()
