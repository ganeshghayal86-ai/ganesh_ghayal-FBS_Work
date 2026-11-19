# 1. Write a program to prompt user to enter userid and password. If Id and
# password is incorrect give him chance to re-enter the credentials. Let him try 3
# times. After that program to terminate.



user='ganesh'
passw=12345

for i in range(1,4):
    userid=input('enter userid:')
    password=int(input('enter password:'))
    if user==userid and passw==password:
        print('success')
        break
    else:
        print('invalid credentials.try again')
else:
    print('invalid credentials,program terminated')