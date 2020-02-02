def Fibonacci(n):
    a,b=1,2
    while b<n:
        a,b=b,a+b
        yield b
if __name__ == '__main__':
    print(sum(i if i%2==0 else 0 for i in Fibonacci(4e6)))
    # NOTE: sum([i if i%2==0 else 0 for i in Fibonacci(4e6)])
    #   it will use much more memory if i use brackets (why?)
