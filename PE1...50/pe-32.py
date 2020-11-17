# すべての桁に 1 から n が一度だけ使われている数をn桁の数が
# パンデジタル (pandigital) であるということにしよう:
#  例えば5桁の数 15234 は1から5のパンデジタルである.

# 7254 は面白い性質を持っている. 39 × 186 = 7254 と書け, 
# 掛けられる数, 掛ける数, 積が1から9のパンデジタルとなる.
# 掛けられる数/掛ける数/積が1から9のパンデジタルとなるような積の総和を求めよ.

# HINT: いくつかの積は, 1通り以上の掛けられる数/掛ける数/
# 積の組み合わせを持つが1回だけ数え上げよ.


result = []
d = list("123456789")
# print(sorted("984" + "321" + "675") == d)
for a in range(1, 9876 + 1):
    for b in range(1, 9876 + 1):
        c = a * b
        if(c > 9999 or c < 1000):
            continue
        res = str(c) + str(a) + str(b)
        if(sorted(res) == d):
            result.append(c)
            print(a,b,c)

result.sort()
print(result)
# 重複削除
res_set = set(result)
print(sum(res_set))