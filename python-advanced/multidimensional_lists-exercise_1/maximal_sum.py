rows, columns = [int(x) for x in input().split()]

matrix = []
the_sum = 0

best_sum = float("-inf")

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

for row_index in range(rows - 2):
    for column_index in range(columns - 2):
        the_sum = matrix[row_index][column_index] + matrix[row_index][column_index + 1]\
                  + matrix[row_index][column_index + 2] + matrix[row_index + 1][column_index]\
                  + matrix[row_index + 1][column_index + 1] + matrix[row_index + 1][column_index + 2]\
                  + matrix[row_index + 2][column_index] + matrix[row_index + 2][column_index + 1]\
                  + matrix[row_index + 2][column_index + 2]

        if the_sum > best_sum:
            best_sum = the_sum
            start_row = row_index
            start_column = column_index

print(f"Sum = {best_sum}")
print(f"{matrix[start_row][start_column]} {matrix[start_row][start_column + 1]} {matrix[start_row][start_column + 2]}")
print(f"{matrix[start_row + 1][start_column]} {matrix[start_row + 1][start_column + 1]}\
 {matrix[start_row + 1][start_column + 2]}")
print(f"{matrix[start_row + 2][start_column]} {matrix[start_row + 2][start_column + 1]}\
 {matrix[start_row + 2][start_column + 2]}")
