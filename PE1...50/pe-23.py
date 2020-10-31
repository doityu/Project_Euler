# 真の約数の和を返す関数
def div_sum(num):
    lower_div, upper_div = [], []
    i = 1
    while i * i <= num:
        if(num % i == 0):
            lower_div.append(i)
            if (i != num // i):
                upper_div.append(num // i)
        i += 1
    return sum(lower_div+upper_div[1:])

border = 28123
# 過剰数のリスト
over_li = []
for i in range(1, border):
    if(div_sum(i) > i):
        over_li.append(i)

# 過剰数の和で表せる正の整数の集合
can_calc = set()
for i in range(len(over_li)):
    for j in range(i, len(over_li)):
        can_calc.add(over_li[i]+over_li[j])

# 正の整数のリスト
num_li = []
# 過剰数の和で表せない物を判断する処理
for i in range(1, border):
    if(i not in can_calc):
        num_li.append(i)

print(can_calc)
print(sum(num_li))
