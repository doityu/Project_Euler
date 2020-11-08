import math

# 素数判定関数(総当たり √N)
def isPrime(number):
    if(number < 2):
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if(number % i == 0):
            return False
    return True

# 巡回しているか判定
def isCircleNum(num):
    s_num = str(num)
    for i in range(len(s_num)):
        circle_num = int(s_num[i:] + s_num[:i])
        if(not isPrime(circle_num)):
            return False
    return True
    

res = []
for i in range(2,1000000):
    if(isCircleNum(i)):
        res.append(i)

print(res)
print(len(res))