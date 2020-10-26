fib_list = [1,2]

border = 4000000
for i in range(1,100):
    next_fib = fib_list[i]+fib_list[i-1]
    if(next_fib > border):
        break
    fib_list.append(next_fib)

print(fib_list)

sum = 0
for i in fib_list:
    if (i % 2 == 0):
        sum += i

print(sum)