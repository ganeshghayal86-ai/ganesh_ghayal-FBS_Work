def fibo(a,b,n):
    if n==0:
        return 
    c=a+b
    print(c)
    
    fibo(b,c,n-1)
fibo(-1,1,5)
