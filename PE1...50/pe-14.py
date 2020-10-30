

max_num = 1000000
max_len = 0

for i in range(1, max_num + 1):
    now_len = 0 
    n = i
    while n != 1:
        if ( n % 2 == 0):
            n /= 2
        else:
            n = 3*n + 1
        now_len += 1
    if(max_len < now_len):
        max_len = now_len
        print(max_len ,i)