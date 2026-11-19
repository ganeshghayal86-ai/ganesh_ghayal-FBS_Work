#  q1.py
#         *

#       *   *

#     *       *

#   *           *

# *               *

# *               *

#  *             *

#     *       *

#       *   *

#         *



for i in range(1,11):
    for j in range(1,6-i):
        print(' ',end=' ')
    if i==1:
        print('*')
    elif i==2:
        print('*   *')
    elif i==3:
        print('*       *')
    elif i==4:
        print('*           *')
    elif i==5:
        print('*               *')
    elif i==6:
        print('*               *')
    elif i==7:
        print(' *             *')
    elif i==8:
        print('    *       *')
    elif i==9:
        print('      *   *')
    elif i==10:
        print('        *')
    print()



    