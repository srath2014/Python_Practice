# Wap to reverse the given number.

n = int(input("Enter the number you want to reverse"))

rev = 0

while(n>0):
    dig = n%10
    rev = rev*10+dig
    print(rev)
    n = n//10

print("reverse of the number",rev)