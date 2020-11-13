f = open("./pe-42_words.txt", "r")
data = f.readline().replace("\"", "").split(",")
f.close()


tri_list = [ int(0.5 * i * (i + 1)) for i in range(1, 1001)]

score_sum = 0
for i in range(len(data)):
    score = 0
    for j in data[i]:
        score += ord(j) - ord('A') + 1
    if(score in tri_list):
        score_sum += 1
print(score_sum)