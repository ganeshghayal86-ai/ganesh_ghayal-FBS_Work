# 10. Write a program to reverse a number using recursion.

def reverse(n,rev):
    if n==0:
        return rev
    d=n%10
    rev=rev*10+d
    n=n//10
    return reverse(n,rev)
res=reverse(1234,0)
print(res)
