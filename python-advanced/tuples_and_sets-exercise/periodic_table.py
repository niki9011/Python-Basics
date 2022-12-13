number = int(input())

unique_elements = set()

for _ in range(number):
    elements = input().split()
    for element in elements:
        unique_elements.add(element)

for name in unique_elements:
    print(name)
