# 1. A list contains the denominations as follows :
# D = [2000, 500, 200, 100 , 50, 20, 10, 5]
# Accept an amount from user and calculate how many
# minimum number of notes will be needed for that
# amount.
amount=int(input("enter amount:"))
total_notes=0
D=[2000,500,200,100,50,20,10,5]
for i in D:
    notes=amount//i
    total_notes+=notes
    amount=amount%i
print(total_notes)
    