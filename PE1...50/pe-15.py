def Calc(n, r):
    result = 1
    for i in range(n, n - r, -1):
        result *= i
    tmp = 1
    for i in range(1, r+1):
        tmp *= i
    return result // tmp


n = int(input())

print(Calc(n*2, n))
