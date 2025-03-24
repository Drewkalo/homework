import heapq

def johnson(graph):

    def bellman_ford(G, start):
        d = {i:float('inf') for i in G}
        parents = {i:None for i in G}
        d[start] = 0
        for i in range(len(G) - 1):
            for node1 in G:  
                for node2 in G[node1]: 
                    if d[node2] > d[node1] + G[node1][node2]:
                        d[node2] = d[node1] + G[node1][node2]
                        parents[node2] = node1

        #проверим есть ли отрицательный цикл, если да, то расстояние до одной из вершин уменьшиться
        for node1 in G:
            for node2 in G[node1]:
                if d[node2] > d[node1] + G[node1][node2]:
                     return False

        return d
    
        #дейкстра с использованием потенциалов от добавления нулевой вершины
    def dijkstra(graph, start, potential):
        distances = {node: float('inf') for node in graph}
        distances[start] = 0
        pq = [(0, start)]
        while pq:
            curr_dist, curr_node  = heapq.heappop(pq)
            if curr_dist > distances[curr_node]:
                continue
            
            for neighbor in graph[curr_node]:
                reweighted_distance = graph[curr_node][neighbor] + potential[curr_node] - potential[neighbor]
                if distances[neighbor] > distances[curr_node] + reweighted_distance:
                    distances[neighbor] = distances[curr_node] + reweighted_distance
                    heapq.heappush(pq, (distances[neighbor], neighbor))

        return distances

        #создаём копию графа с нулевой вершиной, связанной со всеми другими.
    new_graph = {node: graph[node] for node in graph}
    new_graph['s'] = {node: 0 for node in graph}

        #проверка на отрицательные циклы, если их нет, то потенциалом будет результат белмана-форда
    bellman_ford_res = bellman_ford(new_graph, 's')
    if bellman_ford_res is False:
        return None 

    potential = bellman_ford_res

        #перевзвешиваем граф
    reweighted_graph = {}
    for node in graph:
        reweighted_graph[node] = {}
        for neighbor in graph[node]:
            reweighted_weight = graph[node][neighbor] + potential[node] - potential[neighbor]
            reweighted_graph[node][neighbor] = reweighted_weight

        #применяем дейкстру на перевзвешенном графе
    correct_distances = {}
    for start_node in graph:
        correct_distances[start_node] = dijkstra(reweighted_graph, start_node, potential)
        #минусуем потенциалы, чтобы получить корректные расстояния
        for end_node in graph:
            if correct_distances[start_node][end_node] != float('inf'):
                correct_distances[start_node][end_node] = correct_distances[start_node][end_node] - potential[start_node] + potential[end_node]


    return correct_distances


M = int(input())

G = {}

for i in range(M):
    v1, v2, w = input().split()
    w = float(w)
    if v1 in G:
        G[v1][v2] = w
    else:
        G[v1] = {v2: w}
    if v2 in G:
        G[v2][v1] = w
    else:
        G[v2] = {v1: w}


result = johnson(G)

if result:
    print(result)
else:
    print("Обнаружен отрицательный цикл.")
