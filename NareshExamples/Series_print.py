# Wap to read a number n and print the series 1+2+...+n
n = int(input("Enter the number"))
a=[]

for i in range(1,n+1):
    print(i,sep="",end="")
    if(i<n):
        print("+",sep="",end="")
    a.append(i)
print("=",sum(a))
print()
