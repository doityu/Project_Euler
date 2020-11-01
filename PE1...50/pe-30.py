
pow_num = 5
max_num = pow(9,pow_num)

result_list = []
for i in range(2, max_num*pow_num + 1):
    result = 0
    for dig in str(i):
        result += pow(int(dig),pow_num)
        if(result > i):
            break
    if(result == i):
        result_list.append(i)

print(result_list)
print(sum(result_list))