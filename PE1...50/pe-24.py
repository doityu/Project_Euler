# 参考https://qiita.com/BlueSilverCat/items/77f4e11d3930d7b8959b
# ずるい方法
import itertools

num = 10
gole = 1000000

print(list(itertools.permutations(range(num)))[gole-1])
