# 4. Write a program to find sum of n numbers using recursion./

def SumOfNumbers(n,sum):
    if n==0:
        return sum
    sum+=n
    n=(n-1)

    return SumOfNumbers(n,sum)
   
print(SumOfNumbers(10,0))
