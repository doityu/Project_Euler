# 数1406357289は0から9のパンデジタル数である (0から9が1度ずつ現れるので).
# この数は部分文字列が面白い性質を持っている.

# d1を上位1桁目, d2を上位2桁目の数とし, 以下順にdnを定義する.
# この記法を用いると次のことが分かる.

# d2d3d4=406 は 2 で割り切れる
# d3d4d5=063 は 3 で割り切れる
# d4d5d6=635 は 5 で割り切れる
# d5d6d7=357 は 7 で割り切れる
# d6d7d8=572 は 11 で割り切れる
# d7d8d9=728 は 13 で割り切れる
# d8d9d10=289 は 17 で割り切れる
# このような性質をもつ0から9のパンデジタル数の総和を求めよ.

# 参考
# https://qiita.com/yopya/items/241710b86b70ce58c4bf

from itertools import permutations
import time

# リスト内の数値で割り切れるか判断
def isDiv(num):
    str_num = str(num)
    div_num = [2, 3, 5, 7, 11, 13, 17]
    for i in range(10 - 3):
        d = int(str_num[i+1:i+4])
        if(d % div_num[i] != 0):
            return False
    return True



result = []
start = time.time()
# permutations を使用する考えはなかった
for str_num in permutations(("0123456789")):
    # join が分からんかった
    num = ''.join(str_num)
    if(isDiv(num)):
        print(num)
        result.append(int(num))

print(result)
print(sum(result))
print(time.time()-start)