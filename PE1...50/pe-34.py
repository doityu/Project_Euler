import math


ans = []
for i in range(3, 10000000):
    fact_sum = 0
    str_num = str(i)
    for num in str_num:
        fact_sum += math.factorial(int(num))
        if(fact_sum > i):
            break
    if(i == fact_sum):
        print(i)
        ans.append(i)
print(sum(ans))
