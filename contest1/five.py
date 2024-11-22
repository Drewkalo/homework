a = list(map(int, input().split()))
s = [0] * a[0]
#создаём массив, состоящий из строк
for i in range(a[0]):
    s[i] = list(map(int, input().split()))

def area(matr):
    n, k = len(matr), len(matr[0])
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    large = 1
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            if matr[i - 1][j - 1] == 1:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                large = max(large, dp[i][j])
    return large

print(area(s))