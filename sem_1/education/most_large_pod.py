def longest_common_subsequence(X, Y):
    m = len(X)
    n = len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    # Матрица для восстановления подпоследовательности
    path = [[""] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                path[i][j] = "diag"  # Диагональное движение
            else:
                if dp[i - 1][j] > dp[i][j - 1]:
                    dp[i][j] = dp[i - 1][j]
                    path[i][j] = "up"  # Движение вверх
                else:
                    dp[i][j] = dp[i][j - 1]
                    path[i][j] = "left"  # Движение влево

    # Восстановление подпоследовательности
    i = m
    j = n
    lcs = ""
    while i > 0 and j > 0:
        if path[i][j] == "diag":
            lcs = X[i - 1] + lcs
            i -= 1
            j -= 1
        elif path[i][j] == "up":
            i -= 1
        else:
            j -= 1

    return lcs, dp[m][n]


X = ['A', 'B', 'C', 'B', 'D', 'A', 'B']
Y = ['B', 'D', 'C', 'A', 'B', 'A']
lcs, length = longest_common_subsequence(X, Y)
print(f"Наибольшая общая подпоследовательность: {lcs}")  # Выведет одну из НОП
print(f"Длина наибольшей общей подпоследовательности: {length}") # Выведет 4
