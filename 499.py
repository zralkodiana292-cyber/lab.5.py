s = input().strip()
digits = sorted(s)

# Знаходимо першу ненульову цифру, щоб число не починалося з нуля
non_zero_idx = 0
for i, d in enumerate(digits):
  if d != "0":
    non_zero_idx = i
    break
min_digits = [digits[non_zero_idx]] + digits[:non_zero_idx] + digits[non_zero_idx + 1:]
min_num = "".join(min_digits)

# Формуємо найбільше чотиризначне число (сортування у зворотному порядку)
max_num = "".join(sorted(s, reverse=True))

print(min_num, max_num)