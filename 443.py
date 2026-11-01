nums = list(map(int, input().split()))
if nums:
    nums = [nums[-1]] + nums[:-1]
print(*nums)