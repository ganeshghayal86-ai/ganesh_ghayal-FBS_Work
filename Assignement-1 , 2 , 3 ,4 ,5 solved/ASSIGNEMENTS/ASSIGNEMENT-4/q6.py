# 6. WAP to check if a given number is prime number or not.

n=int(input('enter number:'))
for i in range(2,n):
    if n%i==0:
        print('it is not prime')
        break
else:
    print("it is prime")