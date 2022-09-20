import sys

n = int(input())

max_num = -sys.maxsize
num_sum = 0g

for i in range(0,n):
    curr_num = int(input())
    if curr_num > max_num:
        max_num = curr_num
        num_sum += curr_num

if max_num == num_sum - max_num:
    print(f'Yes')
    print(f'Sum = {num_sum}')

else:
    print('No')
    diff = abs(num_sum - max_num)
    print(f'Diff = {diff}')
