import math

# 素数判定関数(総当たり √N)
def isPrime(number):
    if(number < 2):
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if(number % i == 0):
            return False
    return True

a_max = 1000
b_max = 1000
result = {"max_num":0}
for a in range(-a_max + 1, a_max):
    for b in range(-b_max + 1, b_max):
        n = 0
        # n = 0 から始めて連続する整数で素数を生成したときの長さ
        target = 0
        while isPrime(n*n + a*n + b):
            target += 1
            n += 1
        if(target > result["max_num"]):
            result["max_num"] = target
            result["a"] = a
            result["b"] = b
            print(result)

print(result["a"] * result["b"])