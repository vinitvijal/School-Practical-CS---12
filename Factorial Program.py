# WAP to input any number from user and calculate factorial of a number.
# Created By Vinit


def fact(n):
    fac = 1
    for i in range(1,n+1):
        fac = fac * i
    return fac

x = int(input("Enter Your Number : "))

result = fact(x)

print(result)
