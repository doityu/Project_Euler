import math

# 素数判定関数(総当たり √N)
def isPrime(number):
    if(number < 2):
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if(number % i == 0):
            return False
    return True

gole = 10001
n = 0
number = 1

while True:
    if(isPrime(number)):
        n += 1
        if(n == gole):
            print(number)
            break
    number += 1

