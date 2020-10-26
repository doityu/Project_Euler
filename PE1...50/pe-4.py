# 回文数か判断する
def isPalindromic(num):
    str_num = str(num)
    rev_str = ""
    for i in range(1, len(str_num) + 1):
        rev_str += str_num[-i:len(str_num) + 1 -i]
    if(str_num == rev_str):
        return True
    return False

max_num = 999
min_num = 100
ans = 0
for i in range(max_num, min_num+1 , -1):
    for j in range(max_num, i+1 , -1):
        if(isPalindromic(i*j) and ans < i*j):
            ans = i*j
print(ans)