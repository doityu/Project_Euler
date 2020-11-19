# 項差3330の等差数列1487, 4817, 8147は
# 次の2つの変わった性質を持つ.

# (i)3つの項はそれぞれ素数である.
# (ii)各項は他の項の置換で表される.
# 1, 2, 3桁の素数にはこのような性質を持った数列は存在しないが,
# 4桁の増加列にはもう1つ存在する.

# それではこの数列の3つの項を連結した12桁の数を求めよ.



import math

# 素数判定関数(総当たり √N)
def isPrime(number):
    if(number < 2):
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if(number % i == 0):
            return False
    return True

# 他の項で置換できるか＝同じ数値を用いているか
def isSameNum(a, b, c):
    if(sorted(str(a)) == sorted(str(b)) 
        and sorted(str(a)) == sorted(str(c))):
        return True
    return False

prime_list = []
for i in range(1000 , 10000):
    if(isPrime(i)):
        prime_list.append(i)

for i in range(len(prime_list)):
    for j in range(i + 1, len(prime_list)):
        a = prime_list[i]
        b = prime_list[j]
        c = 2 * b - a
        if(c in prime_list):
            if(isSameNum(a, b, c)):
                print(a, b, c)
