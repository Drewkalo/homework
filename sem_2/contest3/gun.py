n = int(input())
drum_before = input().strip()
drum_after = input().strip()

cases = []
for i in range(n):
    flag = True
    for j in range(n-1):
        shift = (i + j + 1)%n
        # print('shift:', shift)
        if not shift:
            continue
        else:
            unknown_pos = shift -1
            if unknown_pos >= len(drum_before) or drum_before[unknown_pos] != drum_after[j]:
                flag = False
                break
    if flag:
        cases.append(i)

bullet_var = set()
for case in cases:
    if not case:
        bullet_var.add(0)
        bullet_var.add(1)
    else:
        bullet_var.add(int(drum_before[case-1]))

# print('bullet_var:', bullet_var)

if 1 in bullet_var:
    if 0 in bullet_var:
        print('Random')
    else:
        print('Yes')
else:
    if 1 in bullet_var:
        print('Random')
    else:
        print('No')    