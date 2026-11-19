# Sum of all odd numbers between 1 to n

def SumOfOddNumbers():
    n=int(input('enter numbers:'))
    sum=0
    for i in range(1,n+1):
        if i%2!=0:
            sum+=i
    print('sum of all odd numbers is:',sum)

SumOfOddNumbers()