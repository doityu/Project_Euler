# 五角数は Pn = n(3n-1)/2 で生成される. 最初の10項は
# 1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...である.
# P4 + P7 = 22 + 70 = 92 = P8 である. 
# 
# しかし差 70 - 22 = 48 は五角数ではない.
# 五角数のペア Pj と Pk について, 差と和が五角数になるものを考える.
# 差を D = |Pk - Pj| と書く. 差 D の最小値を求めよ.

# 回答方法自体は出来ていたがリストで回していたため非常に遅い
# set にしたらすぐに回答が表示された
# リスト等の探索スピードについて
# https://qiita.com/cof/items/05f6ffc6d4e5b062aaa9

# 答えを返す関数
def findAns():
    num_set = set(i * (3 * i - 1) // 2 for i in range(1, 9999))

    for i in num_set:
        for j in num_set:
            if(j > i):
                plus = j + i
                minus = j - i
                if(plus in num_set and minus in num_set):
                    return i - j

print(findAns())