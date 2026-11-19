# Input 5 subject marks from user and display grade(eg.First class,Second class ..)

m1=int(input("enter sub1:"))
m2=int(input("enter sub2:"))
m3=int(input("enter sub3:"))
m4=int(input("enter sub4:"))
m5=int(input("enter sub5:"))

obtained=m1+m2+m3+m4+m5
percentage=(obtained/500)*100

if percentage>=75: 
    print('distincation')
elif percentage>=60:
    print('first class')
elif percentage>=50:
    print('second class')
elif percentage>=35:
    print('pass')
else:
    print('fail')

