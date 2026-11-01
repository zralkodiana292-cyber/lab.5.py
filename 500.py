s = input()

if "," in s:
  matrix = [
      list(map(int, part.strip().split()))
      for part in s.split(",")
      if part.strip()
  ]
else:
  nums = list(map(int, s.split()))
  matrix = [nums[i : i + 3] for i in range(0, len(nums), 3)]

print(matrix)

sorted_matrix = sorted(matrix, key=lambda x: x[1])
print(sorted_matrix)