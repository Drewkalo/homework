import numpy as np
def mnk(x, y):
    x, y = np.array(x), np.array(y)
    b = ((x*y).mean() - (x.mean() * y.mean())) / ((x**2).mean() - (x.mean())**2)
    a = y.mean() - b * x.mean()
    k = ((x*y).mean()) / ((x**2).mean())
    return [a,b,k]

x = [1,2,3,4,5]

y = [2,3.2,3.9,4.5,5.1]

print(mnk(x,y))
