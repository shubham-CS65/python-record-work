name=input("Enter student name:  ")
n=int(input("Enter number of subjects: "))
total=0
for i in range(1,n+1):
    mark=float(input(f"Enter the marks of the subject{i}: "))
    total+=mark
percentange=total/n
if percentange>=90:
    g="A+"
    p="Outstanding"
elif percentange>=80:
    g="A"
    p="Excellent"
elif percentange>=70:
    g="B"
    p="Very Good"
elif percentange>=60:
    g="C"
    p="Good"
elif percentange>=50:
    g="D"
    p="Average"
else:
    g="F"
    p="Needs Improvement"
print("\n---Academic Performance---")
print("Name of the student:",name)
print("Total marks        :",total)
print("Percentage         :",round(percentange,2),"%")
print("Grade              :",g)
print("Performance        :",p)