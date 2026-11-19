# 11. WAP to check if given number Strong Number.
n = int(input('Enter number: '))
temp = n
total = 0

while n > 0:
    digit = n % 10
    fact = 1
    i = 1

    while i <= digit:
        fact = fact * i
        i += 1

    total = total + fact
    n = n // 10

if total == temp:
    print('Strong Number')
else:
    print('Not a Strong Number')
