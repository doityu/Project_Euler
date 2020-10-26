import math
import time

# 素数リストを返す関数(総当たり N)
def find_prime1(number):
    prime_list = []
    for i in range(2, number):
        for j in range(1, i):
            if(i % j == 0):
                break
            if(i == j + 1):
                prime_list.append(i)
    return prime_list

# 素数リストを返す関数(総当たり √N)
def find_prime2(number):
    prime_list = [2]
    for i in range(3, int(math.sqrt(number)) + 1):
        for j in range(2, i):
            if(i % j == 0):
                break
            if(i == j + 1):
                prime_list.append(i)
    return prime_list

# 素数リストを返す関数(エラトステネスの篩)
def find_prime_sieve(number):
    prime_list = [i for i in range(2, number+1)]
    for i in range(2, number+1):
        if(i*i > number):
            break
        for j in range(i*i, number+1, i):
            if(j in prime_list):
                prime_list.remove(j)
    return prime_list 

# 時間計測の関数
def time_find_prime(func, num):
    start = time.time()
    func(num)
    end = time.time()
    return end-start

ex1 = 600851475143
# print(str(time_find_prime(find_prime1, ex1)) + "秒")
# print(str(time_find_prime(find_prime2, ex1)) + "秒")
# print(str(time_find_prime(find_prime_sieve, ex1)) + "秒")
div = 2
while ex1 > div:
    while(ex1 % div == 0):
        ex1 = ex1 // div
    div += 1
print(ex1)