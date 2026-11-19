# 9. Write a program to check if entered number is a palindrome or
# not.
def NumberIsPalindromeOrNot():
    n=int(input('enter number:'))
    while n>0:
        d1=n%10
        n=n//10
        d2=n%10
        n=n//10
        d3=n%10
        n=n//10
    if d1==d3:
        print('palindrome')
    else:
        print('not palindrome')
NumberIsPalindromeOrNot()