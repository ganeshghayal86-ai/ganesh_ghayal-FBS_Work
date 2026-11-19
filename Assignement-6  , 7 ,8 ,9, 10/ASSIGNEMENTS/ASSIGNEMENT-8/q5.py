# 5. Sum of all prime numbers between 1 to n

def SumOfAllPrimeNumbers():
    n=int(input('enter numbers:'))
    total=0
    num=2
    while num<=n:
        i=2
        while i<num:
            if num%i==0:
                break
            i+=1
        else:
        
            total+=num
        num+=1
    print('sum of all prime numbers is:',total)
SumOfAllPrimeNumbers()
