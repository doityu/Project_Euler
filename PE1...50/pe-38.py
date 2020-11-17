# 192 に 1, 2, 3 を掛けてみよう.

# 192 × 1 = 192
# 192 × 2 = 384
# 192 × 3 = 576

# 積を連結することで1から9の パンデジタル数 192384576 が得られる. 
# 192384576 を 192 と (1,2,3) の連結積と呼ぶ.

# 同じようにして, 9 を 1,2,3,4,5 と掛け連結することで
# パンデジタル数 918273645 が得られる. 
# これは 9 と (1,2,3,4,5) との連結積である.

# 整数と (1,2,...,n) (n > 1) との連結積として得られる
# 9桁のパンデジタル数の中で最大のものはいくつか?


# パンデジタル数か判断
def isPandigital(num):
    d = list("123456789")
    if(sorted(str(num)) == d):
        return True
    return False


result = []
d = list("123456789")

for a in range(1, 10000 + 1):
    res = ""
    for b in range(1, 10+1):
        c = a * b
        res += str(c)
        if(len(res) > 9):
            break
        if(isPandigital(res)):
            result.append(res)
            print(a,b,c)

print(result)
print(max(result))