# q5
#         1 
#       1   2
#     1       3
#   1           4
# 1   2   3   4   5
for i in range(1,6):
    for j in range(1,6-i):
        print(' ',end=' ')
    if i==1:
        print(1,end=' ')
    elif i==2:
        print('1   2',end='')
    elif i==3:
        print('1       3',end='')
    elif i==4:
        print('1           4',end='')
    else:
        print('1   2   3   4   5',end='')
    print()
    
       

        
        
     
        

