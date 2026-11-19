# 3. Write a program to reverse a given number using recursive function.

def reverse(n):
    if n==0:
        return
    d=n%10
    print(d,end="")
    n=n//10
    reverse(n)
   
reverse(531)