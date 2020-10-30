import time

# 約数の数を返す関数
def div_num(num):
    lower_div, upper_div = [], []
    i = 1
    while i * i <= num:
        if(num % i == 0):
            lower_div.append(i)
            if (i != num // i):
                upper_div.append(num // i)
        i += 1
    return len(lower_div+upper_div)


max_num = 10 ** 5
border = 500

tri_num = 0
start = time.time()
for i in range(1, max_num):
    tri_num += i
    if(div_num(tri_num) > border):
        print(tri_num)
        break
end = time.time()
print("fin:" + str(end-start))
