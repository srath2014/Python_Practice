# Wap to find if the given integer is pallindrome or not.
n = int(input(("Enter the given number")))

temp=n
rev =0

while(n>0):
    dig = n%10
    rev = rev*10 + dig
    n=n//10

if (rev == temp):
    print(rev,"is pallindrome numver")
else:
    print("The given number is not pallindrome")