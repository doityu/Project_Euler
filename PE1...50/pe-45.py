# 三角数, 五角数, 六角数は以下のように生成される.

# 三角数	Tn=n(n+1)/2	1, 3, 6, 10, 15, ...
# 五角数	Pn=n(3n-1)/2	1, 5, 12, 22, 35, ...
# 六角数	Hn=n(2n-1)	1, 6, 15, 28, 45, ...
# T285 = P165 = H143 = 40755であることが分かる.

# 次の三角数かつ五角数かつ六角数な数を求めよ.

# 参考URL
# https://qiita.com/271828_tk/items/636c1402469f7ebc722f

import time

start = time.time()

N = 70000
# 三角数
triangleNum = [ (i * (i + 1) //2) for i in range(N)]
# 互角数
pentagonalNum = [ (i * (3*i -1) //2) for i in range(N)]
# 六角数
hexagonalNum = [ (i * (2*i - 1)) for i in range(N)]

for t in triangleNum:
    if(t in pentagonalNum and t in hexagonalNum):
        print(t)

print(type(triangleNum[0]))
print(time.time() - start)