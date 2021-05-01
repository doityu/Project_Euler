# Christian Goldbachによって提示されたことは、奇数の合成数すべては素数と平方の2倍の和で表されることであった。
# 9 = 7 + 2×1^2
# 15 = 7 + 2×2^2
# 21 = 3 + 2×3^2
# 25 = 7 + 2×3^2
# 27 = 19 + 2×2^2
# 33 = 31 + 2×1^2
# この予想は誤りであった。

# 素数と平方の2倍の和で表すことができない最小の奇数の合成数は何か？
# 素数判定関数(総当たり √N)
import math

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

# 平方数の2倍と素数の和で表せない最小の奇合成数を見つける関数
# 見つからない場合はリストを返す
def get_ans(MAX_NUM):
    prime_set = set(primes(MAX_NUM))
    # 奇数かつ素数でないものを奇数合成数とする
    odd_composite_list = [ i for i in range(2, MAX_NUM+1) if i % 2 != 0 and i not in prime_set] 
    for odd_num in odd_composite_list:
        # 平方数の2倍と素数の和で表せるかのフラグ
        flag = False
        for i in range(1, MAX_NUM + 1):
            calc_num = odd_num - 2 * i ** 2
            if(calc_num < 0):
                break
            elif(calc_num in prime_set):
                flag = True
                break
        if(not flag):
            return odd_num
    return odd_composite_list

if __name__ == "__main__":
    MAX_NUM = 10 ** 4
    print(get_ans(MAX_NUM))

