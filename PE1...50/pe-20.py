import math

result = str(math.factorial(100))
num_li = []
for i in result:
    num_li.append(int(i))

print(sum(num_li))