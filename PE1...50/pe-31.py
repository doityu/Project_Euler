# 何通りあるか計算
def calc(coin_list, p, num):
    if(coin_list[p] == 1 or num == 0):
        return 1
    else:
        sum_num = 0
        for i in range(num // coin_list[p] + 1):
            target = num - coin_list[p] * i
            sum_num += calc(coin_list, p+1, target)
        return sum_num


coin_li = [200, 100, 50, 20, 10, 5, 2, 1]

num = 200

print(calc(coin_li, 0, num))
