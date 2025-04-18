def main():
    import sys
    sys.setrecursionlimit(1000000)
    N, k = map(int, sys.stdin.readline().split())
    matrix = [sys.stdin.readline().strip() for _ in range(N)]

    # Создаём граф: экспериментаторы (0..N-1) и обработчики (N..2N-1)
    graph = {i: {} for i in range(2 * N)}
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == '1':
                # Допустимая пара: пропускная способность 1
                graph[i][N + j] = 1
                graph[N + j][i] = 0  # Обратное ребро
            else:
                # Недопустимая пара: пропускная способность k
                graph[i][N + j] = k
                graph[N + j][i] = 0  # Обратное ребро

    def dfs(u, visited, parent):
        visited.add(u)
        for v in graph[u]:
            if graph[u][v] > 0 and v not in visited:
                parent[v] = u
                if v >= N and (v not in match_r or dfs(match_r[v], visited, parent)):
                    match_r[v] = u
                    return True
        return False

    res = 0
    while True:
        match_r = {}  # Обработчики -> экспериментаторы
        matched = set()
        for i in range(N):
            visited = set()
            parent = {}
            if dfs(i, visited, parent):
                matched.add(i)
        if len(matched) == N:
            res += 1
            # Уменьшаем пропускную способность использованных рёбер
            for j in match_r:
                i = match_r[j]
                graph[i][j] -= 1
                graph[j][i] += 1
        else:
            break

    print(res)

if __name__ == "__main__":
    main()