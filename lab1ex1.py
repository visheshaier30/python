print("==============Student Scorecard===========")

name=input("Enter Student name:")

subject1=float(input("Enter your marks:"))
subject2=float(input("Enter your marks:"))
subject3=float(input("Enter your marks:"))

total=subject1+subject2+subject3
avg=total*100/300

print("\n=====FINAL SCORECARD======")
print("Student Name:",name)
print("Subject1:",subject1)
print("Subject2:",subject2)
print("Subject3:",subject3)
print("Total Marks:",total)
print("Average:",avg)