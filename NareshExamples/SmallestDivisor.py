# Wap to find the smallest divisor of any given number.
n= int(input("Enter the given number to be tested"))
a =[]

for i in range(2,n+1):
    if(n%i == 0):
        a.append(i)
    a.sort()
print("Smallest divisor of n is",a[0])