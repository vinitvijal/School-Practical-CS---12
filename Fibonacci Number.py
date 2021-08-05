
def fib(n):
    a = 0
    b = 1
    if n == 1:
        print(a)
    elif n == 2:
        print(b)
    else:
        for i in range(2,n):
            c = a + b
            a = b
            b = c
            nth = a+b
        print(nth)
num = int(input("Enter your number : " ))
fib(num)