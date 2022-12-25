numbers = input().split(", ")

matrix = []
row = int(numbers[0])
the_sum = 0

for n in range(row):
    columns = [int(x) for x in input().split(", ")]
    the_sum += sum(columns)
    matrix.append(columns)

print(the_sum)
print(matrix)
