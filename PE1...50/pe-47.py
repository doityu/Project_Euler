# 異なる素数因子を持つ2つの連続した最初の数は次である：
# 14 = 2 × 7
# 15 = 3 × 5
# 3つの異なる素数因子を持つ3つの連続した最初の数は次である。

# 644 = 2^2 × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19
# 4つの異なる素数因子を持つ4つの連続した数を求めよ。その最初の数は何か？

# 参考
# １つ目：https://java-beginner.com/project-euler-java-46-50/
# ２つ目：https://qiita.com/yopya/items/6706f79766b576c70b0d


import math

NUM_OFFACTORS = 4
MAX_NUM = 10**6

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
        if is_prime[number] == 0:
            continue
        yield number
        if number <= square_root_of_max:
            for multiple in range(number * 2, max_number, number):
                is_prime[multiple] = 0

# 素因数のリストを返す
def getPrimeFactors(n, prime_set):
    prime_factors = []
    for prime in prime_set:
        if(prime >= n):
            break
        if(n % prime == 0):
            prime_factors.append(prime)
    return prime_factors    

# 計算1:20~30s
def calcAns1(prime_set):
    factors_1 = []
    factors_2 = []
    factors_3 = []
    factors_4 = []

    factors_2 = getPrimeFactors(3, prime_set)
    factors_3 = getPrimeFactors(4, prime_set)
    factors_4 = getPrimeFactors(5, prime_set)

    for i in range(6, MAX_NUM):
        factors_1 = factors_2
        factors_2 = factors_3
        factors_3 = factors_4
        factors_4 = getPrimeFactors(i, prime_set)

        if(len(factors_1) == NUM_OFFACTORS 
        and len(factors_2) == NUM_OFFACTORS
        and len(factors_3) == NUM_OFFACTORS
        and len(factors_4) == NUM_OFFACTORS):
            return i - NUM_OFFACTORS + 1
    return 0

# 計算2:2~3s
def get_factors_list(prime_set):
    factors_list = [[] for i in range(MAX_NUM+1)]

    for i in range(2, MAX_NUM+1):
        if i in prime_set:
            for j in range(i*2, MAX_NUM, i):
                factors_list[j] += [i]
    return factors_list

if __name__ == "__main__":
    prime_set = set(primes(MAX_NUM))
    factors_list = get_factors_list(prime_set)
    ans = []
    for i in range(MAX_NUM):
        if (len(factors_list[i]) == NUM_OFFACTORS):
            ans.append(i)
            if(len(ans) == NUM_OFFACTORS):
                break
        else:
            ans = []
    print(ans)

    # ans_set = calcAns1(prime_set)
    # for small_num in ans_set:
    #     print(small_num , getPrimeFactors(small_num, prime_set))
    #     print(small_num + 1, getPrimeFactors(small_num + 1, prime_set))
    #     print(small_num + 2, getPrimeFactors(small_num + 2, prime_set))
    #     print(small_num + 3, getPrimeFactors(small_num + 3, prime_set))
    #     print()
