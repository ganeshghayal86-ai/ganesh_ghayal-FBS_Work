# 6. Write a program to print first n prime numbers.

num=int(input('enter numbers:'))
count=0
n=2
while num>count:
    for i in range(2,n):
        if n%i==0:
            print('it is not prime number')
            break
    else:
        print(n,'it is prime number')
        count+=1
    n+=1
print(count) 

      