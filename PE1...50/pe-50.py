# 素数41は6つの連続する素数の和として表せる:

# 41 = 2 + 3 + 5 + 7 + 11 + 13.
# 100未満の素数を連続する素数の和で表したときにこれが最長になる.

# 同様に, 連続する素数の和で1000未満の素数を表したときに
# 最長になるのは953で21項を持つ.

# 100万未満の素数を連続する素数の和で表したときに
# 最長になるのはどの素数か?

# 素数ジェネレーター
# https://qiita.com/Mokkeee/items/93b6b7d59fa256aa1677

import math

# 素数判定関数(総当たり √N)
def primes(max_number):
    """
    指定値未満の素数を取得するジェネレータ
    :param max_number: 最大値
    :return: 素数ジェネレータ
    """
    if max_number <= 2:
        raise StopIteration
    yield 2
    is_prime = [1] * max_number
    square_root_of_max = max_number ** 0.5
    for number in range(3, max_number, 2):
        if is_prime[number] is 0:
            continue
        yield number
        if number <= square_root_of_max:
            for multiple in range(number * 2, max_number, number):
                is_prime[multiple] = 0


# 連続する素数の和の最長を返す
def consecutivePrimeSum(prime_list):
    for i in range(len(prime_list), 1, -1):
        for spot in range(len(prime_list) - i):
            num = 0
            for j in range(i):
                num += prime_list[j + spot]
                if(num > prime_list[len(prime_list)-1]):
                    break
            if(num in prime_list):
                return(i, num)

prime_li = []
for prime in primes(1000000):
    prime_li.append(prime)

print(consecutivePrimeSum(prime_li))
