n, e, m = map(int, input().split())

timetable = [[] for i in range(n+1)]


for i in range(m):
    temp = list(map(int, input().split()))
    wait = []
    for j in range(1, 2*temp[0] + 1, 2):
        wait.append((temp[j], temp[j+1]))

    k = temp[0]
    for i in range(k):
        for j in range(i+1, k):
            v1, time_in = wait[i]
            v2, time_out = wait[j]
            timetable[v1].append((v2, time_in, time_out))


dist = [float("inf")] * (n+1)
dist[1] = 0
visited = set()


while len(visited) < len(timetable):
    curr = 0
    curr_time = float("inf")
    for i in range(1, n+1):
        if i not in visited and dist[i] < curr_time:
            curr_time = dist[i]
            curr = i

    if curr == 0:
        break
    visited.add(curr)

    for station, time_in, time_out in timetable[curr]:
        if dist[curr] <= time_in and time_out <= dist[station]:
            dist[station] = time_out


if dist[e] == float("inf"):
    print(-1)
else:
    print(dist[e])
