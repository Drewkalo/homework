n = int(input())
parts = [input().strip() for _ in range(n)]
dict_for_parts = {}
res = set()

# print(parts)
def is_palindrome(s):
    return s == s[::-1]

for cnt in range(n):
    string = parts[cnt]
    if string not in dict_for_parts:
        dict_for_parts[string] = []
    dict_for_parts[string].append(cnt + 1)

# print(dict_for_parts)

for i in range(n):
    curr_part = parts[i]
    len_part = len(curr_part)

    for j in range(len_part + 1):
        preff_part = curr_part[:j]
        suff_part = curr_part[j:]

        if is_palindrome(preff_part):
            ref = suff_part[::-1]
            # print(ref)
            if ref in dict_for_parts:
                for l in dict_for_parts[ref]:
                    if l != i+1:
                        res.add((l, i+1))

        if is_palindrome(suff_part):
            ref = preff_part[::-1]
            # print(ref)
            if ref in dict_for_parts:
                for r in dict_for_parts[ref]:
                    if i+1 != r:
                        res.add((i+1, r))


print(len(res))
for i in sorted(res):
    print(i[0], i[1])
