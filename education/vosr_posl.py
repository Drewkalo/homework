def longest_increasing_subsequence(nums):
    n = len(nums)
    if n == 0:
        return []

    dp = [1] * n  #Длина наибольшей возрастающей подпоследовательности, заканчивающейся на nums[i]
    predecessors = [-1] * n # Индекс предыдущего элемента в наибольшей возрастающей подпоследовательности

    max_length = 1
    max_index = 0

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                predecessors[i] = j

        if dp[i] > max_length:
            max_length = dp[i]
            max_index = i

    # Реконструкция наибольшей возрастающей подпоследовательности
    lis = []
    current_index = max_index
    while current_index != -1:
        lis.append(nums[current_index])
        current_index = predecessors[current_index]

    return lis[::-1] # Переворачиваем список, чтобы получить возрастающую последовательность


nums = [10, 9, 2, 5, 3, 7, 101, 18]
result = longest_increasing_subsequence(nums)
print(f"Наибольшая возрастающая подпоследовательность: {result}") # Вывод: [2, 3, 7, 101]

