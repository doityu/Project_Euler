
result = set()

num_max = 100
for a in range(2, num_max + 1):
    for b in range(2, num_max + 1):
        result.add(pow(a,b))

print(len(result))