alphabet = '$abc'
pos = {}
c = 0
for i in alphabet:
    pos[i] = c
    c += 1

def calc_position(count):
    for i in range(1,len(count)):
        count[i] += count[i-1]
    return count

def suff_array(s):

    s = s + '$'
    count = [0]*len(alphabet)
    for char in s:
        count[pos[char]] += 1
    count = calc_position(count)

    p = [0]*len(s)
    for i in range(len(s)-1,0,-1):
        count[pos[s[i]]] -= 1
        p[count[pos[s[i]]]] = i

    c = [0]*len(s)
    cn = 0
    last_char = '$'
    for i in range(len(p)):
        if s[p[i]] != last_char:
            last_char = s[p[i]]
            cn += 1
        c[p[i]] = cn
    cur_len = 1
    while cur_len <= len(s):
        sorted2 = [0]*len(s)
        for i in range(len(s)):
            sorted2[i] = (p[i] - cur_len)%len(s)
        count = [0]*len(s)
        for i in sorted2:
            count[c[i]] += 1
        count = calc_position(count)
        for i in range(len(sorted2)-1,-1,-1):
            count[c[sorted2[i]]] -= 1
            p[count[c[sorted2[i]]]] = sorted2[i]
        new_c = [0]*len(s)
        cN = 0
        for i in range(1,len(p)):
            mid1 = (p[i] + cur_len)%len(s)
            mid2 = (p[i-1] + cur_len)%len(s)
            if c[p[i]] != c[p[i-1]] or c[mid1] != c[mid2]:
                cN += 1
            new_c[p[i]] = cN
        c = new_c
        cur_len *= 2
    return p

print(suff_array('abacaba'))