# 参考https://hack.jp/?p=252
# 参考https://java-beginner.com/project-euler-java-26-30/

# 1/nの循環節の位置を求める
def junkan(num):
    # 剰余の保持
    remainder = 1
    cycle_num = 0
    # 余りのリスト
    remain_list = []
    while True:
        remainder *= 10
        if(remainder < num):
            remain_list.append(None)
            continue
        remainder %= num
        if(remainder == 0):
            cycle_num = 0
            break
        elif(remainder in remain_list):
            cycle_num = len(remain_list) - remain_list.index(remainder)
            break
        remain_list.append(remainder)
    return cycle_num


num = 1000
max_long = 0
for i in range(2, num):
    result = junkan(i)
    if(result > max_long):
        max_long = result
        print(i, max_long)

