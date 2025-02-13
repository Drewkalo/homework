def number_of_factors(num):
    for i in range(1, num + 1):
        if num % i == 0:
            c += 1
    return c

n = int(input())

# вызываем функцию
print(number_of_factors(n))