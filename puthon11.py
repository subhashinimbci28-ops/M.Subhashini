n = int(input())
nums = map(int,input().split())
result = tuple(a**2 if a % 2 == 0 else a**3 for a in nums)
print(result)
