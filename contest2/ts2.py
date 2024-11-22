def check_view(arr: list, x):
    if x == 0:
        return int(-1)
    else:
        for i in range(x-1, -1,-1):
            if arr[i] >= arr[x]:
                return int(i)
            elif arr[i] == arr[x]:
                return int(i)
            else:
                continue
        return int(-1)

s = [int(s) for s in input().split()]
res = [check_view(s,i) for i in range(0, len(s))]
print(*res)
