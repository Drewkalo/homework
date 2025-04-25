n = int(input())
flag = False
drum_before = input().strip()
drum_after = input().strip()

shift = '$' + drum_before
bullets = max(drum_before.count('1'), drum_after.count('1'))
if bullets > drum_after.count('1'):
    print('Yes')
    flag = True
if bullets == n:
    print('Yes')
    flag = True

temp = set()
control_case1 = '1' + drum_after
control_case2 = '0' + drum_after
# print('case1:', control_case1)
# print('case2:', control_case2)
for i in range(n):
    sample = shift[i:] + shift[:i]
    #print(sample)
    if sample.replace('$', '1') == control_case1:
        if sample.replace('$', '0') == control_case2:
            print('Random')
            flag = True
            break
        else:
            temp.add('Yes')

    if sample.replace('$', '0') == control_case2:
        if sample.replace('$', '1') == control_case1:
            print('Random')
            flag = True
            break
        else:
            temp.add('No')

if not flag:
    if len(temp) != 1:
        print('Random')
    else:
        print(temp.pop())