import math

# 素数判定関数(総当たり √N)
def isPrime(number):
    if(number < 2):
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if(number % i == 0):
            return False
    return True

num = 2000000
sum = 0
for i in range(1, num+1):
    if(isPrime(i)):
        sum += i
print(sum)