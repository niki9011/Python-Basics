count_nubers = int(input())

odd = 0
even = 0

for nubers in range(1, count_nubers + 1):
    current_nubers= int(input())

    if nubers % 2 == 0:
        even += current_nubers
    else:
        odd += current_nubers

if odd == even:
    print('Yes')
    print(f'Sum = {odd}')
else:
    print('No')
    print(f'Diff = {abs(even - odd)}')

