# Write a program to check if person is eligible to marry or not (male age >=21 andfemale age>=18)

gender=input('enter gender(m/f):')
age=int(input('enter age:'))

if gender=='f':
    if age>=18:
        print('girl is eligible to marry.') 
    else:
        print('girl is not to marry.')
else:
    if age>=21:
        print('boy is eligible to marry.')
    else:
        print('boy is not eligible to marry.')