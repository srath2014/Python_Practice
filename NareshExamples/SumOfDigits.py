# Wap to sumof digits of a number

n = int(input("Enter the given numbers"))

total =0

while(n>0):
    dig = n%10
    total=total+dig
    n=n//10

print("the total sum of digit:",total)