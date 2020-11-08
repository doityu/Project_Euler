import math

# 素数判定関数(総当たり √N)
def isPrime(number):
    if(number < 2):
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if(number % i == 0):
            return False
    return True

# 切り詰め可能な数値か
def isTruncatable(num):
    s_num = str(num)
    for i in range(len(s_num)):
        # 左から右に桁を除いた時
        l_tmp = int(s_num[i:])
        if(not isPrime(l_tmp)):
            return False
        # 右から左に桁を除いた時
        if(i != 0):
            r_tmp = int(s_num[:i])
            if(not isPrime(r_tmp)):
                return False
    return True

res = []
for i in range(11, 1000000):
    if(isTruncatable(i)):
        res.append(i)

print(res)
print(sum(res))

