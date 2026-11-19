# 3. Write a program to find sum of following series using functions :
# a. 1+ 2 + 3 + 4+..... + n
# b. 1!+ 2! + 3! + 4!+..... + n!
# c. 1^1 + 2^2 + 3^3+ ...... n^n

def SumOfSeries():
    n=int(input('enter number:'))
    total=0
    for i in range(1,n+1):
        total+=i
    print('sum of series  is:',total)

    

    n=int(input('enter number:'))
    fact=1
    total_fact=0
    for i in range(1,n+1):
        fact=fact*i
        total_fact+=fact
    print('sum of factorial series is:',total_fact)

    


    n=int(input('enter number:'))
    tot=0
    for i in range(1,n+1):
       
        squ=i**i
        tot+=squ
    print('sum of power series is:',tot)
SumOfSeries()