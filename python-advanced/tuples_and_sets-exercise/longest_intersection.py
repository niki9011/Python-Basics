number = int(input())

result = []
data1 = set()
data2 = set()

for _ in range(number):
    range1, range2 = input().split("-")
    start, end = int(range1[0]), int(range1[2] + 1)
    start2, end2 = int(range2[0]), int(range2[2] + 1)

    for num1 in range(start, end + 1):
        data1.add(num1)

    for num2 in range(start2, end2 + 1):
        data2.add(num2)

print(data1)
print(data2)



