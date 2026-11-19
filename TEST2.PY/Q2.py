# Write a program to accept 3 digit number. If first digit is double of second digit and half of
# third digit then display “Yes, you have done it”, otherwise display “Please try next time”.

num =int(input('enter number:'))
d1=num//100
d2=(num//10)%10
d3=num%10
if d1==d2*2 and d1*2==d3:
    print('yes,you have done it.')
else:
    print("Please try again next time.")
