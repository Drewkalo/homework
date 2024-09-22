a = [c for c in input()] 
a[::2], a[1::2] = a[1::2], a[::2]
print(''.join(a))