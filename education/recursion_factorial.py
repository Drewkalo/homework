def factorial(a: int):
    if a == 1:
        return 1
    return a * factorial(a-1)
print(factorial(5))