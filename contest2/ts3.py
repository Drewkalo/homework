def count_friend(arr, id):
    if id == len(arr):
        return int(0)
    else:
        cnt = 0
        idfriend = id + 1
        while idfriend < len(arr):
            if arr[id] < arr[idfriend]:
                cnt += 1
                id = idfriend
                idfriend = id + 1
            else:
                idfriend += 1
        return cnt
            
s = [int(x) for x in input().split()]
res = [count_friend(s, i) for i in range(0, len(s))]
print(*res)

