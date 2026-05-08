numbers = (2, 4, 5, 6, 2, 3, 4, 4, 7)
repeated = set([x for x in numbers if numbers.count(x) > 1])
print(f"Repeated items: {repeated}")
