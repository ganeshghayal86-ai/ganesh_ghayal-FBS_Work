# 7. Write a program to solve the following series :
# a. 1! + 2! + 3! + 4! + .....n!
# b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)
# c. Find the sum of a geometric series from 1 to n where the common ratio is 2.
# d. S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10
# e. x - x2/3 + x3/5 - x4/7 + .... to n terms

fact_total=0
n=int(input('enter numbers:'))
fact=1
for i in range(1,n+1):
    fact=fact*i
 
    fact_total+=fact
print(fact_total)
   


total=0
n=int(input('enter numbers:'))
for i in range(1,n+1):
    exp=i**i
    total+=exp
print('sum of exponent series is:',total)


