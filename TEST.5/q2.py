n = int(input("Enter number of coins: "))

li = list(map(int, input("Enter coin numbers: ").split()))

for i in li:
    if li.count(i) % 2 != 0:
        print("Missing coin number:", i)
        break