# Student Marks Management System
print("----------------------------------Student Marks Management System----------------------------------")
marks = [70, 80, 65, 90]

# Display marks - Traversal
print("Original Marks:")
for mark in marks:
    print(mark)

#inseration
marks.insert(4,99)

print("\nAfter Insertion:")
print(marks)

#deletion
marks.remove(80)

print("\nAfter deletion:")
print(marks)

#updetion
marks[2]=66

print("\nAfter updetion:")
print(marks)