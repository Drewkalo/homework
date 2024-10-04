def step(fin,  n = {1:1, 2:1}):
    if fin in n:
        return n[fin]
    else:
        n[fin] = step(fin-1,n) + step(fin-2,n)
        return n[fin]
    
print(step(1000))