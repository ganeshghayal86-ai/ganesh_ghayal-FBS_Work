def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)

print(fact(5))

def sum(n):
    if n==0:
        return 0
    return fact(n) + sum(n-1)
print(sum(5))