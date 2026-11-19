# 10. WAP to check if given number is Perfect Number.

total=0
n=int(input('enter numbers:'))
for i in range(1,n):
    if n%i==0:
        total+=i
    
if total==n:
    print('perfact number')
else:
    print('not perfact number')

        
    
        