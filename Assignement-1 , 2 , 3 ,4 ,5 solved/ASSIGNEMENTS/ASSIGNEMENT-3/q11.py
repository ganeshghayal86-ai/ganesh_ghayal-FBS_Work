# 11. Accept age of five people and also per person ticket amount and then calculate total
# amount to ticket to travel for all of them based on following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.


a1=int(input('enter age1:'))
a2=int(input('enter age2:'))
a3=int(input('enter age3:'))
a4=int(input('enter age4:'))
a5=int(input('enter age5:'))
ta1=int(input('enter ticket amount1:'))
ta2=int(input('enter ticket amount2:'))
ta3=int(input('enter ticket amount3:'))
ta4=int(input('enter ticket amount4:'))
ta5=int(input('enter ticket amount5:'))


if a1 < 12:
    actual1 = ta1 - (ta1 * 30 / 100)
elif a1 > 59:
    actual1 = ta1 - (ta1 * 50 / 100)
else:
    actual1 = ta1
if a2<12:
    actual2=ta2-(ta2*30/100)
elif a2>59:
    actual2=ta2-(ta2*50/100)
else:
    actual2=ta2

if a3 < 12:
    actual3 = ta3 - (ta3 * 30 / 100)
elif a3 > 59:
    actual3 = ta3 - (ta3 * 50 / 100)
else:
    actual3 = ta3

if a4 < 12:
    actual4 = ta4 - (ta4 * 30 / 100)
elif a4 > 59:
    actual4 = ta4 - (ta4 * 50 / 100)
else:
    actual4 = ta4

if a5 < 12:
    actual5 = ta5 - (ta5 * 30 / 100)
elif a5 > 59:
    actual5 = ta5 - (ta5 * 50 / 100)
else:
    actual5 = ta5
 
total_amount=actual1+actual2+actual3+actual4+actual5
print('total ticket amount:',total_amount)