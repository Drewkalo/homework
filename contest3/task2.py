temp = [int(c) for c in input().split()]
n, m = temp[0], temp[1]
clients = list(map(int, input().split()))
total_time = 0
cash_machine = [0] * m

while bool(any(cash_machine)) == True or bool(clients) == True:
    less_time_diff = 10e10
    for i in range(m):
        if cash_machine[i] == 0 and bool(clients) == True:
            cash_machine[i] = clients.pop(0)
    for i in range(m):
        if cash_machine[i] > 0:
            less_time_diff = min(less_time_diff, cash_machine[i])
    for i in range(m):
        if  cash_machine[i] > 0:
            cash_machine[i] -= less_time_diff

    total_time += less_time_diff

print(total_time)