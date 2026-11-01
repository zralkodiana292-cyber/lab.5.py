nums = list(map(int, input().split()))

evens = sorted([x for x in nums if x % 2 == 0], reverse=True)
odds = [x for x in nums if x % 2 != 0]

result = evens + odds
print(*result)