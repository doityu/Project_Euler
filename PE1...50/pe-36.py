# pe-4から流用 回文数か判断する
def isPalindromic(num):
    str_num = str(num)
    rev_str = ""
    for i in range(1, len(str_num) + 1):
        rev_str += str_num[-i:len(str_num) + 1 -i]
    if(str_num == rev_str):
        return True
    return False



sample = []
res = []
for num in range(1,1000000):
    bin_num = bin(num).replace("0b","")
    if(isPalindromic(num) and isPalindromic(bin_num)):
        sample.append([num,bin_num])
        res.append(num)

print(sample)
print(sum(res))