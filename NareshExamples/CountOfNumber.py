# Wap to count the digits in a given number
n=int(input("Enter the number"))

count =0

while(n>0):
    count = count+1
    n=n//10

print(count,"No of digits are there in the given number")