#fib series with memorization -> o(n)

def fib(mem,n):
    if n < 1:
        print("error")
    
    if n == 1:
        return 0
    if n == 2:
        return 1

    if mem[n] == 0:
        mem[n] = fib(mem,n-1) + fib(mem,n-2)
    print(mem[n],end=" ")
    return mem[n]




n =6
mem = [0]*10
k = fib(mem,n)
print("{}th fib number is {}".format(n,k))

# print(fib(mem,n))
