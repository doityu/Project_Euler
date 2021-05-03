# 1から始めて, 以下のように反時計回りに数字を並べていくと, 辺の長さが7の渦巻きが形成される.

# 37	36	35	34	33	32	31
# 38	17	16	15	14	13	30
# 39	18	5	4	3	12	29
# 40	19	6	1	2	11	28
# 41	20	7	8	9	10	27
# 42	21	22	23	24	25	26
# 43	44	45	46	47	48	49
# 面白いことに, 奇平方数が右下の対角線上に出現する. 
# もっと面白いことには, 対角線上の13個の数字のうち, 8個が素数である. ここで割合は8/13 ≈ 62%である.

# 渦巻きに新しい層を付け加えよう. すると辺の長さが9の渦巻きが出来る. 
# 以下, この操作を繰り返していく. 対角線上の素数の割合が10%未満に落ちる最初の辺の長さを求めよ.
import math

BORDER = 0.1
DIAGONAL_NUM = 4

# 素数判定関数(総当たり √N)
def isPrime(number):
    if(number < 2):
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if(number % i == 0):
            return False
    return True


def get_result():
    # 1辺の長さ
    side_length = 3
    # 対角線の合計数
    sum_diagonal_num = 1
    # 素数の数
    sum_prime_num = 0
    # 前の週の最大値
    before_max_num = 1
    while(True):
        diagonal = []
        for num in range(before_max_num + side_length-1, side_length ** 2 + 1, side_length-1):
            if(isPrime(num)):
                sum_prime_num += 1
            diagonal.append(num)
        before_max_num = max(diagonal)

        # 対角線上の素数の割合を計算
        sum_diagonal_num += DIAGONAL_NUM
        # print(sum_prime_num/sum_diagonal_num)
        if(sum_prime_num/sum_diagonal_num < BORDER):
            return side_length
        side_length += 2
        

if __name__ == "__main__":
    print(get_result())