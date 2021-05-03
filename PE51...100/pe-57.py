# 2の平方根は無限に続く連分数で表すことができる.

# √ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...
# 最初の4回の繰り返しを展開すると以下が得られる.

# 1 + 1/2 = 3/2 = 1.5
# 1 + 1/(2 + 1/2) = 7/5 = 1.4
# 1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
# 1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

# 次の3つの項は99/70, 239/169, 577/408である. 第8項は1393/985である. これは分子の桁数が分母の桁数を超える最初の例である.

# 最初の1000項を考えたとき, 分子の桁数が分母の桁数を超える項はいくつあるか?

from fractions import Fraction
import sys

BORDER = 1000

# 分子の桁数が分母の桁数を超えるときにTrue
def is_numerator_more_denominator(fraction_num):
    numerator_len = len(str(fraction_num.numerator))
    denominator_len = len(str(fraction_num.denominator))
    if(numerator_len > denominator_len):
        return True
    return False

# num + 1項目の分数を返す
def get_value(num):
    if(num == 0):
        return Fraction(1, 2)
    else:
        return Fraction(1, 2 + get_value(num - 1))

if __name__ == "__main__":
    # エラー回避用に再起回数の上限を変更
    # RecursionError: maximum recursion depth exceeded in comparison
    sys.setrecursionlimit(1500)
    ans = 0
    for i in range(BORDER):
        result = 1 + get_value(i)
        if(is_numerator_more_denominator(result)):
            ans += 1
    print(ans)

