num = int(input())

# 対角線の値を保存するリスト
diagonal_list = [[1]]
# 前の週の最大値
before_max_num = 1
for i in range(3, num+1 , 2):
    diagonal = []
    for j in range(before_max_num + i-1, i ** 2 + 1, i-1):
        diagonal.append(j)
    before_max_num = max(diagonal)
    diagonal_list.append(diagonal)

print(diagonal_list)
result = 0
for i in diagonal_list:
    result += sum(i)
print(result)
