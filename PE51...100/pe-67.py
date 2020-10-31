f = open("./pe-67_triangle.txt", "r")
data = f.read()
f.close

li = data.split("\n")
for i in range(len(li)):
    li[i] = li[i].split(" ")
    for j in range(len(li[i])):
        li[i][j] = int(li[i][j])

# 最大経路の和 計算処理
# 上から順に計算
# 2つ選べるときは値が大きいほうを加算
# 3段目の例）17+95+75, 47+(95+75or64+75), 82+64+75
for i in range(1, len(li)):
    for j in range(len(li[i])):
        if(j == 0):
            li[i][j] += li[i-1][j]
        elif(j == len(li[i]) -1):
            li[i][j] += li[i-1][j-1]
        else:
            li[i][j] += max(li[i-1][j-1],li[i-1][j])

print(li)
print(max(li[len(li)-1]))