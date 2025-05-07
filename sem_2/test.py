'''n = int(input())
drum_before = input().strip()
drum_after = input().strip()
length = len(drum_after)

case1 = ("1" + drum_before) * 2
case0 = ('0' + drum_before) * 2
# print(case0)
# print(case1)

part0 = '0' + drum_after
part1 = '1' + drum_after
# print(part0)
# print(part1)
answer = set()
for i in range(2*(length + 1) - length):
    curr0 = case0[i: length + i + 1]
    curr1 = case1[i: length + i + 1]
    #print(curr0)
    #print(curr1)
    if part0 == curr0 or part0 == curr1:
        answer.add('No')
    if part1 == curr0 or part1 == curr1:
        answer.add('Yes')
    if 'Yes' in answer and 'No' in answer:
        break

# print(answer)
if all(ans == 'Yes' for ans in answer):
    print('Yes')
elif all(ans == 'No' for ans in answer):
    print('No')
else:
    print('Random')'''
print(int(5.9999))