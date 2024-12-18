mem = {1:1, 2:1}
def fibb(mem, n):
    if n <= 0:
        return mem[n]
    if n in mem:
        return mem[n]
    else:
        mem[n] = fibb(mem, n-1) + fibb(mem, n-2)
        return mem[n]

print(fibb(mem, 1000))
