# Wap that will print the number divisible within the range.
lower = int(input("Enter the lower boundary"))
upper = int(input("Enter the upper boundary"))
n = int(input("Enter the number wants to divide"))

for i in range(lower,upper):
    if(i%n == 0):
        print(i)

