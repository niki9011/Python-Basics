numbers= int(input())

odd = set()
even = set()
result = set()

for num in range(1, numbers + 1):
    suma_char_name = int(sum([ord(char) for char in input()]) / int(num))
    if suma_char_name % 2 == 0:
        odd.add(suma_char_name)
    else:
        even.add(suma_char_name)

if sum(odd) == sum(even):
    result = odd.union(even)

elif sum(odd) > sum(even):
    result = odd.union(even)

elif sum(odd) < sum(even):
    result = even.difference(odd)

print(", ".join([str(x) for x in result]))
