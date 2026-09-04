grades = [85, 92, 78, 90, 64]
print("Original grades:", grades)

index_input = input("\nEnter the index position to update (0 to 4): ")
position = int(index_input)

grade_input = input("Enter the new grade: ")
new_grade = int(grade_input)

grades[position] = new_grade

print("\nUpdated and Ordered Grades:")
print(grades)