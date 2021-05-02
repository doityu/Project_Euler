# Googol (10^100)は非常に大きな数である: 1の後に0が100個続く. 
# 100^100は想像を絶する. 1の後に0が200回続く. その大きさにも関わらず, 両者とも数字和 ( 桁の和 ) は1である.

# a, b < 100 について自然数 ab を考える. 数字和の最大値を答えよ.

if __name__ == "__main__":
    BORDER_NUM = 100
    max_digit_sum = 0
    for a in range(BORDER_NUM):
        for b in range(BORDER_NUM):
            calc = str(pow(a,b))
            num_list = []
            for i in calc:
                num_list.append(int(i))
            if (max_digit_sum < sum(num_list)):
                max_digit_sum = sum(num_list)
    print(max_digit_sum)
