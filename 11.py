from itertools import groupby
s = input().strip()
print("".join(f"{char}{len(list(group))}" for char, group in groupby(s)))
