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