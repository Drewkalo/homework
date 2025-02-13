import random
mem = {}
def min_cost(arr, mem, n):
    if n <= 0:
        mem[n] = arr[n]
    if n in mem:
        return mem[n]
    else:
        mem[n] = min(min_cost(arr, mem, n-1), min_cost(arr, mem, n-2)) + arr[n]
    return mem[n]
costs = [random.randint(1, 20) for _ in range(5)]
print(costs)
print(min_cost(costs, mem, len(costs)-1))