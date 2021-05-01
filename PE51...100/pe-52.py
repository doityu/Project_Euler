# 125874を2倍すると251748となる. これは元の数125874と順番は違うが同じ数を含む.

# 2x, 3x, 4x, 5x, 6x が x と同じ数を含むような最小の正整数 x を求めよ.


# 他の項で置換できるか＝同じ数値を用いているか
def isSameNum(a, b):
    if(sorted(str(a)) == sorted(str(b))):
        return True
    return False

if __name__ == "__main__":
    MAX_NUM = 10 ** 6
    for num in range(1, MAX_NUM + 1):
        if(isSameNum(num, num * 2)
        and isSameNum(num, num * 3)
        and isSameNum(num, num * 4)
        and isSameNum(num, num * 5)
        and isSameNum(num, num * 6)):
            print(num)