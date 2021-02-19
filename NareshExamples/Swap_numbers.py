# Wap to swap two numbers without using temporary variables.
a = int(input("Enter the first number"))
b = int(input("Enter the first number"))

a = a + b 
b = a - b # now the value of a will be in b 
a = a -b  # now the value of b will be in a

print("The value of a is:",a,"value of b is :",b)
