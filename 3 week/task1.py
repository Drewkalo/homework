a = {1:1, 2:1}          #словарь со значениями чисел
def fib(n):
    if n in a:
        return a[n]
    else:
        a[n] = fib(n - 1) + fib(n - 2)
        return a[n]

print(fib(100))