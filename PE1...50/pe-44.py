# 五角数は Pn = n(3n-1)/2 で生成される. 最初の10項は
# 1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...である.
# P4 + P7 = 22 + 70 = 92 = P8 である. 
# 
# しかし差 70 - 22 = 48 は五角数ではない.
# 五角数のペア Pj と Pk について, 差と和が五角数になるものを考える.
# 差を D = |Pk - Pj| と書く. 差 D の最小値を求めよ.

num_li = []
for i in range(1, 2000):
    num_li.append( str(i * (3 * i - 1) // 2))

penta_num = []
for i in range(len(num_li)):
    for j in range(i, len(num_li)):
        plus = int(num_li[j]) + int(num_li[i])
        minus = int(num_li[j]) - int(num_li[i])
        if(plus > int(num_li[len(num_li)-1])):
            break
        if(str(plus) in num_li and str(minus) in num_li):
            penta_num.append([i,j])

for i in range(len(penta_num)):
    print(num_li[penta_num[i][0]], num_li[penta_num[i][1]])
print(penta_num)