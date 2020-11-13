# 辺の長さが {a,b,c} と整数の3つ組である直角三角形を考え, 
# その周囲の長さを p とする. p = 120のときには3つの解が存在する:
# {20,48,52}, {24,45,51}, {30,40,50}
# p ≤ 1000 のとき解の数が最大になる p はいくつか?

import time 

def get_unique_list(seq):
    seen = []
    return [x for x in seq if x not in seen and not seen.append(x)]

# 答えの組を返す
def get_ressult_list(num):
    res = []
    for a in range(1, int(num*0.29) +1):
        for b in range(a + 1, int(num*0.48) + 1 ):
            c = num - a - b
            if(c ** 2 == a ** 2 + b ** 2):
                res.append([a, b, c])
    return get_unique_list(res)

res = []
max_len = 0

start = time.time()
for i in range(1, 1000+1):
    # print(get_ressult_list(i))
    # res.append([i, len(get_ressult_list(i))])
    if(max_len < len(get_ressult_list(i))):
        max_len = len(get_ressult_list(i))
        print(i,max_len)

print("実行時間：" + str(time.time()-start)[:5] + "s")


### 参考 1 ~ 300 回した時の実行時間
    ## 40秒ほど
    # for a in range(1, num):
    #   for b in range(1, num):
    #     for c in range(1, num):
    #      if(a + b + c == p and a^2 + b ^2 == c^2) 
    # 
    ## 25秒 
    # for a in range(1, num//2 + 1):
    #   for b in range(1, num//2 + 1):
    #     for c in range(1, num//2 + 1):
    # 
    ## 3秒
    #   for b in range(1, num//2 + 1):
    #     c = p -a -b
    #      if(a^2 + b ^2 == c^2) 
    # 
    ## 1秒
    #   for b in range(a, num//2 + 1):
    #  
    ## 番外1
    # 
    #  for b in range(a + 1, num + 1 -2*a):
    #     
    ## 番外2
    # for a in range(1, int(num*0.29) +1):
    #   for b in range(a + 1, int(num*0.48) + 1 ):
