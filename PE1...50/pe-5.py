num_list = [i for i in range(2, 21)]

max_num = 10 ** 10
fin = False

print(num_list)
for i in range(10 ** 8, max_num):
    for num in num_list:
        if(i % num != 0):
            break
        if(num == 20):
            print(i)
            fin = True
            break
    if(fin):
        break
