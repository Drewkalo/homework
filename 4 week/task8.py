a = [1,2,3,4,5]
b = [4,5,6,7,8]
print(set(a)^set(b)) #уникальные для каждого списка
print(set(a).union(b)^(set(a)^set(b)))