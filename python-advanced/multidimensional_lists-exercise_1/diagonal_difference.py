size = int(input())

matrix = []
primary = []
secondary = []

for _ in range(size):
    matrix.append([int(x) for x in input().split()])

for index in range(size):
    primary.append(matrix[index][index])
    secondary.append(matrix[index][size - 1 - index])

print(abs(sum(primary) - sum(secondary)))
