num_p_sum = 0
nums_sum = 0

for i in range(1,101):
    num_p_sum += i ** 2
    nums_sum += i

print(num_p_sum - nums_sum ** 2)