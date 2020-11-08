from fractions import Fraction

# 重複なし、順番保持したリストを返す
def get_unique_list(seq):
    seen = []
    return [x for x in seq if x not in seen and not seen.append(x)]

num = 100
fun_num = []

# 面白くなりそうな物を探す
# i = 分母 j = 分子
for i in range(10, num):
    for j in range(10, i):
        for k in str(i):
            if(k in str(j)):
                # 自明なものを外す
                if("0" in str(i)  and "0" in str(j)):
                    break
                fun_num.append([j, i])
        # print(str(j) + "/" + str(i))

fun_num = get_unique_list(fun_num)

fun_li = []
for i in range(len(fun_num)):
    # 分子
    mole = fun_num[i][0]
    # 分母
    deno = fun_num[i][1]

    for m_s in str(mole):
        for d_s in str(deno):
            if(m_s == d_s):
                m = int(str(mole).replace(m_s, "", 1))
                d = int(str(deno).replace(m_s, "", 1))
                # 分母が0になる場合省く
                if(d == 0):
                    break
                # 一致するか判断
                if(mole/deno == m/d):
                    fun_li.append([mole, deno])
                break

# 自明でないもののリスト
print(fun_li)

# 答えの計算
nume = 1
deno = 1
for i in range(len(fun_li)):
    nume *= fun_li[i][0]
    deno *= fun_li[i][1]
print(Fraction(nume,deno))
