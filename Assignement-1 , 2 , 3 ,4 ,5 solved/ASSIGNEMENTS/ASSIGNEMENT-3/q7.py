# 7. Write a program to check if user has entered correct userid and password.


uid='ganesh'
passw=12345

userid=input('enter userid:')
password=int(input('enter password:'))


if uid==userid and passw==password:
    print('correct userid and password')
else:
    print('incorrect userid and password ')

