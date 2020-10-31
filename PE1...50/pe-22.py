f = open("./pe-22-names.txt", "r")
data = f.readline().replace("\"", "").split(",")
f.close()

data.sort()
score_list = []
for i in range(len(data)):
    name_score = 0
    for j in data[i]:
        name_score += ord(j) - ord('A') + 1
    score_list.append((i+1) * name_score)


print(sum(score_list))
