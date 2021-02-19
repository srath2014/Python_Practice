# python programs to calculate the average of a given list of numbers.

print("python programs to calculate the average of a given list of numbers.")
n = int(input("Enter the list of numbers"))
a =[]
for i in range(0,n):
    elem = int(input("Enter elements"))
    a.append(elem)

avg = sum(a)/n
print("Average of the given list of numebrs",avg)
3