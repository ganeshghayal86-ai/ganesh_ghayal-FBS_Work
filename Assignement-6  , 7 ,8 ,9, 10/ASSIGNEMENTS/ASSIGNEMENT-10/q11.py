# 11. Write a program to print all numbers which are divisible by m and n in the
# # list.
li=[2,75,6,9,43,73,48,54,59,84]
m=int(input('enter number1:'))
n=int(input('enter number2:'))
for i in li:
    if i%m==0 and i%n==0:
        print(i)