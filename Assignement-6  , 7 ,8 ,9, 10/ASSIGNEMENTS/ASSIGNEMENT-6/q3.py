# q3
#       1
#     1   1
#   1   2   1
# 1   3   3   1


for i in range(1,5):
    for j in range(1,5-i):
        print(' ',end=' ')
    if i==1:
        print(1,end='')
    elif i==2:
        print('1   1',end='')
    elif i==3:
        print('1   2   1',end='')
    else:
        print('1   3   3   1',end='')
    print()
   