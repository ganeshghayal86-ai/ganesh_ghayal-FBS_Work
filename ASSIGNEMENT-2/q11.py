# Q11.Write a program to accept an integer amount from user and tell minimum number of notes needed for representing that amount.

# take input

amount=int(input("enter amount:"))

# perform opeartion with formula


n500=amount//500
amount=amount%500

n200=amount//200
amount=amount%200

n100=amount//100
amount=amount%100

n50=amount//50
amount=amount%50

n20=amount//20
amount=amount%20

n10=amount//10
amount=amount%10

total_notes=n500+n200+n100+n50+n20+n10

# display result

print("500 notes:",n500)
print("200 notes:",n200)
print("100 notes:",n100)
print("50 notes:",n50)
print("20 notes:",n20)
print("10 notes:",n10)
print("minimum number of notes:",total_notes)