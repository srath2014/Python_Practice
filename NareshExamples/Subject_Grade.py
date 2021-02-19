# Wap to find out the grade of a student after entering marks for 5 subjects.

Physics = int(input("Enter the marks for Physics"))
Chemistry = int(input("Enter the marks for Chemistry"))
Math = int(input("Enter the marks for Maths"))
Computer_Science = int(input("Enter the marks for Computer science"))
Biology = int(input("Enter the marks for Bilogy"))

Avg_Mark = (Physics + Chemistry + Math + Computer_Science + Biology)//5

if (Avg_Mark >=90):
    print("Grade A")
elif(Avg_Mark >=80 & Avg_Mark<90):
    print("Grade B")
elif(Avg_Mark>=70 & Avg_Mark<80):
    print("Grade C")
else:
    print("Grade D")