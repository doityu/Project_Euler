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


border = 10000
fri_list = []
for a in range(border):
    b = div_sum(a)
    if(div_sum(b) == a and a != b):
        fri_list.append(a)

print(sum(fri_list))