n = int(input())

r1_count = 0
r2_count = 0
r3_count = 0
r4_count = 0
r5_count = 0
total_count = 0

for numbers in range(0, n):
    current_num = int(input())
    if current_num < 200:
        r1_count += 1
    elif current_num <= 399:
        r2_count += 1
    elif current_num <= 599:
        r3_count += 1
    elif current_num <= 799:
        r4_count += 1
    else:
         r5_count += 1

p1 = (r1_count / n) * 100
p2 = (r2_count / n) * 100
p3 = (r3_count / n) * 100
p4 = (r4_count / n) * 100
p5 = (r5_count / n) * 100

print(f'{p1:.2f}')
print(f'{p2:.2f}')
print(f'{p3:.2f}')
print(f'{p4:.2f}')
print(f'{p5:.2f}')
