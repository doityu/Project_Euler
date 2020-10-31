# ずるい方法
import itertools

num = 10
gole = 1000000

print(list(itertools.permutations(range(num)))[gole-1])
