# WAP to input any number from user and check whether it is prime or not.
# Created By Vinit



num = int(input("Enter Your Number : "))

if num > 1:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           break
   else:
       print(num,"is a prime number")
       
else:
   print(num,"is not a prime number")
