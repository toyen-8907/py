# ex11_13.py
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print("下列是前10個Fibonacci數列")
for index in range(10):
    print("%4d" % fib(index), end='')


    
    





