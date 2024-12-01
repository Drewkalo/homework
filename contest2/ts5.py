def check(s:str):
    cnt = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] > s[j]:
                cnt += 1
    return cnt

k = int(input())

for sequ in range(k):
    n, m = map(int, input().split())
    all_wrd = [input() for i in range(m)]
    all_str = [(check(wrd), all_wrd.index(wrd), wrd) for wrd in all_wrd]
    for i in range(len(all_str)):
        low_dist = all_str[i][0]
        minid = i
        for j in range(i+1,len(all_str)):
            if all_str[j][0] < low_dist:
                low_dist = all_str[j][0]
                minid = j
            elif all_str[j][0] == low_dist and all_str[j][1] < all_str[minid][1]:
                minid = j
        all_str[i], all_str[minid] = all_str[minid], all_str[i]

    for dist, id ,st in all_str:
        print(st)
    if sequ < k - 1:
        print()
    