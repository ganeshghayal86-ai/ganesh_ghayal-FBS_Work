# 8. Write a program to check whether a number is prime or not using recursion.

def prime(n,i):
    if n<=1:
        return 'not prime'
    if i==n:
        return 'prime'
    if n%i==0:
        return 'not prime'
    
    return prime(n,i+1)

print(prime(4,2))
 
    