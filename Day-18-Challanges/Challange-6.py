def fibo(n):
    fib=[0,1]
    while True:
        next_num = fib[-1] + fib[-2]
        if next_num > n:
            break
        fib.append(next_num)
    return fib

print(fibo(1000))

