# 12345から3つ選ぶ選び方は10通りである.

# 123, 124, 125, 134, 135, 145, 234, 235, 245, 345.
# 組み合わせでは, 以下の記法を用いてこのことを表す: 5C3 = 10.

# 一般に, r ≤ n について nCr = n!/(r!(n-r)!) である. ここで, n! = n×(n−1)×...×3×2×1, 0! = 1 と階乗を定義する.

# n = 23 になるまで, これらの値が100万を超えることはない: 23C10 = 1144066.

# 1 ≤ n ≤ 100 について, 100万を超える nCr は何通りあるか?
import math

if __name__ == "__main__":
    BORDER_NUM = 1000000
    ans = 0
    for n in range(1, 100 + 1):
        for r in range(n):
            # nCr = n!/(r!(n-r)!)  の計算
            calc = math.factorial(n) // (math.factorial(r) * (math.factorial(n-r)))
            if(calc > BORDER_NUM):
                ans += 1
    print(ans)
