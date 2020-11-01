
border = 1000

fib = [1,1,2]
i = 2
while True:
    fib[2] = fib[1] + fib[0]
    i+=1
    if(len(str(fib[2])) == border ):
        print(fib[2])
        print(i)
        break
    fib[0], fib[1] = fib[1],fib[2]
