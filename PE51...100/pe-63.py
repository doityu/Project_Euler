# 5桁の数 16807 = 75は自然数を5乗した数である.
# 同様に9桁の数 134217728 = 89も自然数を9乗した数である.

# 自然数を n 乗して得られる n 桁の正整数は何個あるか?

BORDER = 1000

ans = 0

for num in range(1, 10):
    for n in range(1, BORDER): 
        result = num ** n
        # 累乗の結果がn桁よりも大きい場合はそれ以降判定しなくてよい
        if(len(str(result)) > n):
            break
        elif(len(str(result)) == n ):
            print(num, n, result)
            ans += 1

print(ans)
