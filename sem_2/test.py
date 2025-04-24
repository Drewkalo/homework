import random

def rabin_karp(s, T):
    if len(s) == 0 or len(T) < len(s):
        return 0
    
    q = 2**13 - 1
    x = random.randint(3, q - 1)
    m = len(s)
    n = len(T)
    res = 0

    # Генерация хешей для всех циклических сдвигов
    shift_hashes = {}
    for shift_num in range(m):
        shifted = s[shift_num:] + s[:shift_num]
        h = ord(shifted[0]) % q
        for j in range(1, m):
            h = (h * x + ord(shifted[j])) % q
        if h not in shift_hashes:
            shift_hashes[h] = []
        shift_hashes[h].append(shifted)

    # Предвычисление хешей для текста T
    ht = [0] * (n + 1)
    x_pow_m = pow(x, m, q)
    for i in range(n):
        ht[i + 1] = (x * ht[i] + ord(T[i])) % q

    # Поиск совпадений
    for i in range(n - m + 1):
        current_h = (ht[i + m] - (x_pow_m * ht[i]) % q) % q
        if current_h in shift_hashes:
            candidate_shifts = shift_hashes[current_h]
            for candidate in candidate_shifts:
                if T[i:i + m] == candidate:
                    res += 1
                    break  # Учитываем только одно совпадение на позиции i

    return res

print(rabin_karp('abc', 'abcabacbacababc'))  # Пример вызова