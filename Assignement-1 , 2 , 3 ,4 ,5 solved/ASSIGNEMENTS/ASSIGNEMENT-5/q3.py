# 3. Accept no. of passengers from user and per ticket cost. Then accept age of each
# passenger and then calculate total amount to ticket to travel for all of them based on
# following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.
passenger =int(input('enter number of passengers:'))
final_amount=0
tc=int(input('enter ticket price:'))
for i in range(1,passenger+1):
  
    age=int(input('enter age:'))
  
    discount=0
    if age<12:
        discount=tc*30/100
    elif age>59:
        discount=tc*50/100
    else:
        discount=0
   
    final_price=tc-discount
    print('passengers:',i,'total_amount is:',final_price)
    final_amount+=final_price
print('final amount is:',final_amount)


  
